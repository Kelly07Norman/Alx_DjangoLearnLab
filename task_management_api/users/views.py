from rest_framework import generics, permissions
from .models import User  # Import the User model
from .serializers import UserSerializer  # Import the User serializer

# User Registration View (Create User)
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()  # Get all users
    serializer_class = UserSerializer  # Specify the serializer to use
    permission_classes = [permissions.AllowAny]  # Allow anyone to register

# User Profile View (Retrieve and Update User)
class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()  # Get all users
    serializer_class = UserSerializer  # Specify the serializer to use
    permission_classes = [permissions.IsAuthenticated]  # Require authentication

    def get_queryset(self):
        # Filter to return only the authenticated user
        return self.queryset.filter(id=self.request.user.id)

# List Users View for Admin
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()  # Get all users
    serializer_class = UserSerializer  # Specify the serializer to use
    permission_classes = [permissions.IsAdminUser]  # Require admin permissions