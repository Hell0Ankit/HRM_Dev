from django.shortcuts import render

# Create your views here.
def hr_dashboard(request):
    return render(request, 'dashboard/hr_dashboard/hr_dashboard.html' )


def em_dashboard(request):
    return render(request, 'dashboard/em_dashboard/em_dashboard.html')