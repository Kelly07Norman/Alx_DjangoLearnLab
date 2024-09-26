from rest_framework import serializers
from .models import Task  # Import the Task model

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # Specify the Task model to serialize
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'created_at', 'updated_at']  # List the fields to be included in the serialization

    def validate_due_date(self, value):
        """
        Check that the due date is in the future.
        """
        from django.utils import timezone  # Import timezone to compare dates
        if value < timezone.now():
            raise serializers.ValidationError("Due date must be in the future.")  # Raise an error if the due date is not valid
        return value  # Return the validated due date

    def create(self, validated_data):
        """
        Create and return a new Task instance, given the validated data.
        """
        return Task.objects.create(**validated_data)  # Create a new task with the validated data

    def update(self, instance, validated_data):
        """
        Update and return an existing Task instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)  # Update title if provided
        instance.description = validated_data.get('description', instance.description)  # Update description if provided
        instance.due_date = validated_data.get('due_date', instance.due_date)  # Update due date if provided
        instance.priority = validated_data.get('priority', instance.priority)  # Update priority if provided
        instance.status = validated_data.get('status', instance.status)  # Update status if provided
        instance.save()  # Save the changes to the database
        return instance  # Return the updated task instance
