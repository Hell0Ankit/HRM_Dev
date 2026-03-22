from django.shortcuts import render

# Create your views here.
def leaves(request):
    return render(request, 'leaves/leaves.html')

def holidays(request):
    return render(request, 'leaves/holydays_listing.html')



def leaves_application(request):
    return render(request, 'leaves/leaves_application.html')


