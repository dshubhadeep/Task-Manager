from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = (
        ('P', 'Planned'),
        ('O', 'Ongoing'),
        ('D', 'Done')
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_date = models.DateField(
        default=timezone.now, blank=True, null=True)
    created_by = models.ForeignKey(
        User, null=True, related_name='task_created_by', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(
        User, blank=True, null=True, related_name='task_assigned_to', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
