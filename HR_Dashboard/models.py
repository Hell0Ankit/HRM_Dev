from django.db import models
from accounts.models import User

class Designation(models.Model):
    designation_id = models.CharField(max_length=100, unique=True)
    designation = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.designation
    

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    employee_id = models.CharField(max_length=50)

    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)

    dob = models.DateField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    address = models.TextField()

    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)

    # PRIMARY CONTACT
    primary_name = models.CharField(max_length=100, null=True)
    primary_relation = models.CharField(max_length=50, null=True)
    primary_phone = models.CharField(max_length=15, null=True)
    primary_email = models.EmailField(null=True)
    primary_address = models.TextField(null=True)

    # SECONDARY CONTACT
    secondary_name = models.CharField(max_length=100, null=True)
    secondary_relation = models.CharField(max_length=50, null=True)
    secondary_phone = models.CharField(max_length=15, null=True)
    secondary_email = models.EmailField(null=True)
    secondary_address = models.TextField(null=True)

    # BANK
    account_holder = models.CharField(max_length=100, null=True)
    account_number = models.CharField(max_length=50, null=True)
    bank_name = models.CharField(max_length=100, null=True)
    branch_name = models.CharField(max_length=100, null=True)
    ifsc_code = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.full_name