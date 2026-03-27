from django.db import models
from accounts.models import User
from django.utils import timezone

class Designation(models.Model):
    designation_id = models.CharField(max_length=100, unique=True)
    designation = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.designation
    

class EmployeeProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)    
    full_name = models.CharField(max_length=100,default="")
    employee_id = models.CharField(max_length=50, unique=True,)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    joining_date = models.DateTimeField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    birthday = models.DateTimeField(null=True, blank=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    address = models.TextField((""))

    # Emergency Contact
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
    


class Leave(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    from_date = models.DateField()
    end_date = models.DateField()
    leave_duration= models.CharField(max_length=50)
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    attach_doc = models.FileField(upload_to='leave_docs/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"

    
class HolidaysListing(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    holiday_list = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.holiday_list