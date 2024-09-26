from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Task  # Import the Task model
from .serializers import TaskSerializer  # Import the Task serializer

# Task List View (Retrieve all tasks for authenticated user)
class TaskListView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer  # Specify the serializer to use
    permission_classes = [permissions.IsAuthenticated]  # Require authentication

    def get_queryset(self):
        # Return only tasks that belong to the authenticated user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user to the currently authenticated user
        serializer.save(user=self.request.user)

# Task Detail View (Retrieve, Update, Delete a specific task)
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer  # Specify the serializer to use
    permission_classes = [permissions.IsAuthenticated]  # Require authentication

    def get_queryset(self):
        # Return only tasks that belong to the authenticated user
        return Task.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        """Override delete method to provide custom response."""
        self.object = self.get_object()
        self.object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Task Completion Toggle View (Mark a task as complete/incomplete)
class TaskToggleCompleteView(generics.UpdateAPIView):
    serializer_class = TaskSerializer  # Specify the serializer to use
    permission_classes = [permissions.IsAuthenticated]  # Require authentication

    def get_queryset(self):
        # Return only tasks that belong to the authenticated user
        return Task.objects.filter(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        task = self.get_object()  # Get the task instance

        # Toggle the is_completed status
        task.is_completed = not task.is_completed
        task.save()

        # Return the updated task with completion status
        return Response({"id": task.id, "is_completed": task.is_completed}, status=status.HTTP_200_OK)