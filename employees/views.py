from django.shortcuts import render

# Create your views here.
def employee_listing(request):
    return render(request, 'employees/employee_listing.html')
def employee_profile(request):
    return render(request, 'employees/employee_profile_details.html')
def add_employees(request):
    return render(request, 'employees/add_employee.html')
def designations(request):
    return render(request, 'employees/designations.html')

