from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('hr', 'HR'),
        ('employee', 'Employee'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    def is_hr(self):
        return self.role == 'hr'

    def is_employee(self):
        return self.role == 'employee'

