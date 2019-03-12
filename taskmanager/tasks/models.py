from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = (
        ('P', 'Planned'),
        ('O', 'Ongoing'),
        ('D', 'Done')
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    assignee = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
