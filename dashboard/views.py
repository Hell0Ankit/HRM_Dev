from django.shortcuts import render

# Create your views here.
def hr_dashboard(request):
    return render(request, 'dashboard/hr_dashboard/hr_dashboard.html' )