from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import User
from django.http import HttpResponse
from django.contrib import messages

def user_login(request):
    if request.user.is_authenticated:
        if request.user.role == 'hr':
            return redirect('hr_dashboard')
        else:
            return redirect('em_dashboard')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'hr':
                return redirect('hr_dashboard')
            else:
                return redirect('em_dashboard')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'accounts/login.html')

@login_required
def create_employee(request):
    if request.user.role != 'hr':
        return HttpResponse("Unauthorized", status=403)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, "Password does not match")
            return redirect('create_employee')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('create_employee')
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='employee'
        )
        messages.success(request, "Employee created successfully")
        return redirect('create_employee')
    return render(request, 'hr_dashboard/employees/create_employee.html')

@login_required
def dashboard_redirect(request):
    if request.user.role == 'hr':
        return redirect('hr_dashboard')

    return redirect('em_dashboard')

@login_required
def user_logout(request):
    logout(request)  
    return redirect('login')  

@login_required
def change_password(request):
    return render(request, 'accounts/change_password.html')

def utilities(request):
    return render(request, 'utilities.html')