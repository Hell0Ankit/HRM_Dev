from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from attendance.models import Attendance,EmployeeProfile
from django.utils import timezone
from accounts.models import User



from datetime import time
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Attendance, EmployeeProfile

@login_required
def attendance(request):

    if request.user.role != 'employee':
        return HttpResponse("Unauthorized User", status=403)

    profile = EmployeeProfile.objects.filter(user=request.user).first()

    today = timezone.now().date()
    current_time = timezone.now().time()

    if request.method == 'POST':

        # Punch In
        if 'check_in' in request.POST:
            # status logic
            if current_time > time(10, 0):  # 10 AM
                status = 'Late'
            else:
                status = 'Present'
            attendance_obj, created = Attendance.objects.get_or_create(
                user=request.user,
                date=today,
                defaults={
                    'profile': profile,
                    'check_in': current_time,
                    'status': status
                }
            )

            if not created:
                return redirect("attendance_status")

        # Punch Out
        elif 'check_out' in request.POST:

            try:
                attendance_obj = Attendance.objects.get(
                    user=request.user,
                    date=today
                )

                if attendance_obj.check_out:
                    return HttpResponse("Already Punched Out")

                attendance_obj.check_out = current_time
                attendance_obj.save()

            except Attendance.DoesNotExist:
                return HttpResponse("Please Punch In First")

    return render(request, 'em_dashboard/attendance.html')

@login_required
def attendance_status(request):
    if request.user.role != 'employee':
        return HttpResponse("Unauthorized User", status=403)
    return render(request, 'em_dashboard/attendance_status.html')

@login_required
def all_attendance_status(request):
    if request.user.role != 'hr':
      return HttpResponse("Unauthorized User", status=403)

    return render(request, 'hr_dashboard/employees/all_attendance_status.html')
