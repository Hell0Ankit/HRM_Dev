from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from HR_Dashboard.models import EmployeeProfile
from django.utils import timezone

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Late', 'Late'),
        ('Absent', 'Absent'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=timezone.now)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Absent')
    def __str__(self):
        return f"{self.user.username} - {self.date}"

