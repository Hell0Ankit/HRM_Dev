from django.shortcuts import render

# Create your views here.

def attendance(request):
    return render(request, 'attendance/employee_attendance.html')
def leave(request):
    return render(request, 'attendance/leave.html')
def holidays(request):
    return render(request, 'attendance/holidays.html')