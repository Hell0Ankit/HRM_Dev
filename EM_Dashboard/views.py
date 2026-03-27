from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from HR_Dashboard.models import EmployeeProfile,Leave,HolidaysListing
from datetime import date

@login_required
def em_dashboard(request):
    if request.user.role != 'employee':
        return HttpResponse("Unauthorized User", status=403)  
    leaves = Leave.objects.filter(user=request.user).order_by('-applied_at')
    try:
        profile = EmployeeProfile.objects.get(user=request.user)
    except EmployeeProfile.DoesNotExist:
        profile = None
    today = date.today()

    holidays = HolidaysListing.objects.filter(date__gte=today).order_by('date')[:5]
    
    context =  {'profile': profile,
                'leaves':leaves,
                'holidays':holidays,
                }
    return render(request, 'em_dashboard/em_dashboard.html', context )


@login_required
def my_profile(request):
    try:
        profile = EmployeeProfile.objects.get(user=request.user)
    except EmployeeProfile.DoesNotExist:
        return HttpResponse("Profile not found", status=404)

    return render(request, 'em_dashboard/my_profile.html', {
        'profile': profile
    })


@login_required
def my_attendance(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)
    return render(request, 'em_dashboard/my_attendance.html')


@login_required
def leaves_application(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)

    profile = EmployeeProfile.objects.get(user=request.user)

    if request.method == 'POST':
        Leave.objects.create(
            user=request.user,
            profile=profile,
            leave_type=request.POST.get('leave_type'),
            from_date=request.POST.get('from_date'),
            end_date=request.POST.get('end_date'),
            leave_duration=request.POST.get('leave_duration'),
            reason=request.POST.get('reason'),
            attach_doc=request.FILES.get('attach_doc')  
        )
        return redirect('em_leaves_status')
    return render(request, 'em_dashboard/leaves_application.html')

def em_leaves_status(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)

    leaves = Leave.objects.filter(user=request.user).order_by('-applied_at')
    total_leaves = leaves.count()
    pending_leaves = leaves.filter(status='pending').count()
    approved_leaves = leaves.filter(status='approved').count()
    rejected_leaves = leaves.filter(status='rejected').count()

    context = {
        'leaves': leaves.order_by('-applied_at'),
        'total_leaves': total_leaves,
        'pending_leaves': pending_leaves,
        'approved_leaves': approved_leaves,
        'rejected_leaves': rejected_leaves,
    }
    return render(request, 'em_dashboard/em_leaves_status.html', context)

@login_required
def em_holydays_listing(request):
    if request.user.role != 'employee':
        return HttpResponse("No access", status=403)
    holidays = HolidaysListing.objects.all()

    return render(request, 'em_dashboard/em_holydays_listing.html',{'holidays':holidays})


