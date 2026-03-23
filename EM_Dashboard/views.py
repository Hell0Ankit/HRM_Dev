from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
# def em_dashboard(request):
#     return render(request, 'em_dashboard/em_dashboard.html')


@login_required
def em_dashboard(request):
    if not request.user.is_employee():
        # return redirect('no_access')
        return HttpResponse("No access")

    return render(request, 'em_dashboard/em_dashboard.html')

# def em_dashboard(request):
#     if request.user.role != 'employee':
#         return redirect('login')
#     return render(request, 'em_dashboard/em_dashboard.html')

def personal_details(request):
    return render(request, 'em_dashboard/personal-details.html')

def my_attendance(request):
    return render(request, 'em_dashboard/my_attendance.html')

def leaves_application(request):
    return render(request, 'em_dashboard/leaves_application.html')

def em_leaves_status(request):
    return render(request, 'em_dashboard/em_leaves_status.html')

def em_holydays_listing(request):
    return render(request, 'em_dashboard/em_holydays_listing.html')