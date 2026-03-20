from django.shortcuts import render

# Create your views here.
def leave_applications(request):
    return render(request, 'leaves/leaves_applications.html')


