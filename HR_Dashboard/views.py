from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
# def hr_dashboard(request):
#     return render(request, 'hr_dashboard/hr_dashboard.html' )


@login_required
def hr_dashboard(request):
    if request.user.role != 'hr':
        return redirect('login')
    return render(request, 'hr_dashboard/dashboard.html')

# Create your views here.
def employee_listing(request):
    return render(request, 'hr_dashboard/employees/employee_listing.html')

def employee_details(request):
    return render(request, 'hr_dashboard/employees/employee_details.html')

def add_employee(request):
    return render(request, 'hr_dashboard/employees/add_employee.html')

def designations(request):
    return render(request, 'hr_dashboard/employees/designations.html')

def attendance_status(request):
    return render(request, 'hr_dashboard/employees/attendance_status.html')

def leaves_status(request):
    return render(request, 'hr_dashboard/employees/leaves_status.html')

def holydays_listing(request):
    return render(request, 'hr_dashboard/employees/holydays_listing.html')


