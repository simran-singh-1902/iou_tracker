from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        owes = validated_data.pop('owes', {})
        owed_by = validated_data.pop('owed_by', {})
        user = super().create(validated_data)
        for name, amount in owes.items():
            user.owes[name] = user.owes.get(name, 0) + amount
        for name, amount in owed_by.items():
            user.owed_by[name] = user.owed_by.get(name, 0) + amount
        user.save()
        return user
