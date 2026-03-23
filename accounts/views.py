from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == 'hr':
                return redirect('hr_dashboard')
            else:
                return redirect('employee_dashboard')
    return render(request, 'accounts/login.html')




@login_required
def dashboard_redirect(request):
    if request.user.role == 'hr':
        return redirect('hr_dashboard')
    else:
        return redirect('em_dashboard')
    
   

def signup(request):
    return render(request, 'accounts/signup.html')

def change_password(request):
    return render(request, 'accounts/change_password.html')

def utilities(request):
    return render(request, 'utilities.html')


