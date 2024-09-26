from django.urls import path
from .views import TaskListView, TaskDetailView, TaskToggleCompleteView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),  # List all tasks (authenticated user)
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),  # Retrieve, update, or delete task
    path('tasks/<int:pk>/toggle-completion/', TaskToggleCompleteView.as_view(), name='task-toggle-complete'),  # Toggle complete status
]