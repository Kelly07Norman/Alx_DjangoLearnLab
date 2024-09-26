from django.urls import path
from .views import UserCreateView, UserDetailView, UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),  # List all users (admin only)
    path('users/join/', UserCreateView.as_view(), name='user-create'),  # Register a new user
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Retrieve or update user
]
