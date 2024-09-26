from rest_framework import serializers
from .models import User  # Import the User model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Specify the User model to serialize
        fields = ['id', 'username', 'email', 'password']  # Include necessary fields

    def create(self, validated_data):
        # Hash the password before saving the user
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Set the hashed password
        user.save()  # Save the user
        return user  # Return the created user instance
