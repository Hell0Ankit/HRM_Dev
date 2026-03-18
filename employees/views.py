from django.shortcuts import render

# Create your views here.
def employee_listing(request):
    return render(request, 'employees/employee_listing.html')

