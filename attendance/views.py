from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from attendance.models import Attendance
from django.utils import timezone
from accounts.models import User


@login_required
def attendance(request):
    if request.user.role != 'employee':
      return HttpResponse("Unauthorized User", status=403)  
  
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
