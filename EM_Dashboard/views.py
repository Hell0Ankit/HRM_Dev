from django.shortcuts import render


# Create your views here.
def em_dashboard(request):
    return render(request, 'em_dashboard/em_dashboard.html')

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