from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'accounts/login.html')

def signup(request):
    return render(request, 'accounts/signup.html')

def change_password(request):
    return render(request, 'accounts/change_password.html')

def utilities(request):
    return render(request, 'utilities.html')