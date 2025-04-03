from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    text = models.CharField(max_length=255)  # Task description
    completed = models.BooleanField(default=False)  # Task status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when task is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when task is updated

    def __str__(self):
        return self.text

