from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from HR_Dashboard.models import EmployeeProfile,Leave


@login_required
def em_dashboard(request):
    if request.user.role != 'employee':
        return HttpResponse("Unauthorized User", status=403)  
    return render(request, 'em_dashboard/em_dashboard.html')

@login_required
def my_profile(request):
    try:
        profile = EmployeeProfile.objects.get(user=request.user)
    except EmployeeProfile.DoesNotExist:
        return HttpResponse("Profile not found", status=404)

    return render(request, 'em_dashboard/my_profile.html', {
        'profile': profile
    })





@login_required
def my_attendance(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)
    return render(request, 'em_dashboard/my_attendance.html')


@login_required
def leaves_application(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)
    profile = EmployeeProfile.objects.get(user=request.user)
    if request.method == 'POST':
        Leave.objects.create(
            user=request.user,
            profile=profile,
            leave_type=request.POST.get('leave_type'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            reason=request.POST.get('reason'),
        )
        return redirect('employee_leave_list')
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


