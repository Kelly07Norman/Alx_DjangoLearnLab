from django.db import models
from users.models import User

# Define the TaskCategory model to categorize tasks.
class TaskCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define the Task model based on your ERD.
class Task(models.Model):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

    PRIORITY_LEVELS = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    PENDING = 'Pending'
    COMPLETED = 'Completed'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_LEVELS, default=MEDIUM)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Establishes a one-to-many relationship with User.
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, blank=True)  # Tasks can belong to a category.
    is_recurring = models.BooleanField(default=False)  # Indicates if a task is recurring.

    def __str__(self):
        return self.title

# Define the RecurringTask model to handle recurring tasks.
class RecurringTask(models.Model):
    DAILY = 'Daily'
    WEEKLY = 'Weekly'
    MONTHLY = 'Monthly'

    FREQUENCY_CHOICES = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
    ]

    task = models.OneToOneField(Task, on_delete=models.CASCADE)  # Each recurring task is associated with one Task.
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    next_occurrence_date = models.DateTimeField()

    def __str__(self):
        return f'{self.task.title} - {self.frequency}'
