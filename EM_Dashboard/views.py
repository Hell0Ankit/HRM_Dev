from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse


@login_required
def em_dashboard(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)

    return render(request, 'em_dashboard/em_dashboard.html')

@login_required
def personal_details(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)

    return render(request, 'em_dashboard/personal-details.html')


@login_required
def my_attendance(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)

    return render(request, 'em_dashboard/my_attendance.html')

@login_required
def leaves_application(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)

    return render(request, 'em_dashboard/leaves_application.html')

@login_required
def em_leaves_status(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)

    return render(request, 'em_dashboard/em_leaves_status.html')

@login_required
def em_holydays_listing(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)

    return render(request, 'em_dashboard/em_holydays_listing.html')