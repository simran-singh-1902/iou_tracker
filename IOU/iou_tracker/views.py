from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from iou_tracker.models import User

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def add_user(request):
    name = request.data.get('name')

    if not name:
        return Response({'error': 'Name is required'})

    # Check if the user already exists
    if User.objects.filter(name=name).exists():
        return Response({'error': 'User with this name already exists'})

    # Create a new user
    user = User(name=name)
    user.save()

    # Serialize the user data and return it in the response
    serializer = UserSerializer(user)
    return Response(serializer.data, status=201)

@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response([{'name': user['name']} for user in serializer.data])

@api_view(['POST'])
def update_user(request):
    data = request.data
    from_user = data.get('lender')
    to_user = data.get('borrower')
    amount = data.get('amount')

    try:
        from_user = User.objects.get(name=from_user)
        to_user = User.objects.get(name=to_user)
    except User.DoesNotExist:
        return Response({"detail": "User does not exist"}, status=400)

    from_user.owes[to_user.name] = from_user.owes.get(to_user.name, 0) + amount
    to_user.owed_by[from_user.name] = to_user.owed_by.get(from_user.name, 0) + amount
    from_user.update_balance()
    to_user.update_balance()
    from_user.save()
    to_user.save()
    return Response({"detail": "User updated successfully"}, status=200)

