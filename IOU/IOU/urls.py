"""IOU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from iou_tracker.views import UserList, UserDetail, update_user, list_users, add_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', list_users, name='list_users'),
    path('add/', add_user, name='add_user'),
    path('ledger/', UserList.as_view(), name='user-list'),
    path('ledger/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('iou/', update_user, name='update_user'),
]
