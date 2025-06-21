from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='team')

class Feedback(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_feedbacks')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_feedbacks')
    strengths = models.TextField()
    areas_to_improve = models.TextField()
    sentiment = models.CharField(max_length=20, choices=[('positive','Positive'),('neutral','Neutral'),('negative','Negative')])
    acknowledged = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
