from django.shortcuts import render, redirect,get_object_or_404
from accounts.models import User
from HR_Dashboard.models import Designation, EmployeeProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
# def hr_dashboard(request):
#     return render(request, 'hr_dashboard/hr_dashboard.html' )


@login_required
def hr_dashboard(request):
    if request.user.role != 'hr':
        return redirect('login')
    return render(request, 'hr_dashboard/hr_dashboard.html')

# Create your views here.
# def employee_listing(request):
#     return render(request, 'hr_dashboard/employees/employee_listing.html')



@login_required
def employee_listing(request):
    if request.user.role != 'hr':
        return HttpResponse("Unauthorized", status=403)

    employees = EmployeeProfile.objects.all()  
    return render(request, 'hr_dashboard/employees/employee_listing.html', {
        'employees': employees
    })


def employee_details(request,id):

    return render(request, 'hr_dashboard/employees/employee_details.html')

def add_employee(request):
    return render(request, 'hr_dashboard/employees/add_employee.html')






def designations(request):
    return render(request, 'hr_dashboard/employees/designations.html')

@login_required
def add_designations(request):
    if request.method == 'POST':
        designation_id = request.POST.get('designation_id')
        designation = request.POST.get('designation')
        if Designation.objects.filter(designation_id=designation_id).exists():
             return HttpResponse("Designation_id already exists")
        if Designation.objects.filter(designation=designation).exists():
             return HttpResponse("Designation already exists")
        else:
            Designation.objects.create(
                designation_id=designation_id,
                designation=designation
            )
        return redirect('designations')
    return render(request, 'hr_dashboard/employees/add_designations.html')


@login_required
def edit_designations(request, id):
    designation_obj = get_object_or_404(Designation, id=id)
    if request.method == 'POST':
        designation_id = request.POST.get('designation_id')
        designation = request.POST.get('designation')
        if Designation.objects.exclude(id=id).filter(designation_id=designation_id).exists():
            return HttpResponse("Designation_id already exists")
        if Designation.objects.exclude(id=id).filter(designation=designation).exists():
            return HttpResponse("Designation already exists")
        designation_obj.designation_id = designation_id
        designation_obj.designation = designation
        designation_obj.save()
        return redirect('designations')
    return render(request, 'hr_dashboard/employees/edit_designations.html', {
        'designation': designation_obj
    })


@login_required
def delete_designation(request, id):
    designation_obj = get_object_or_404(Designation, id=id)
    designation_obj.delete()
    return redirect('designations')


def attendance_status(request):
    return render(request, 'hr_dashboard/employees/attendance_status.html')

def leaves_status(request):
    return render(request, 'hr_dashboard/employees/leaves_status.html')

def holydays_listing(request):
    return render(request, 'hr_dashboard/employees/holydays_listing.html')




@login_required
def add_employee_detail(request):
    if request.user.role != 'hr':
        return HttpResponse("Unauthorized", status=403)
    
    users = User.objects.filter(role='employee')

    if request.method == 'POST':
        user_id = request.POST.get('user')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        employee_id = request.POST.get('employee_id')
        designation_id = request.POST.get('designation')
        profile_image = request.FILES.get('profile_image')

        # Check if profile exists
        if EmployeeProfile.objects.filter(user_id=user_id).exists():
            return HttpResponse("Profile already exists")

        EmployeeProfile.objects.create(
            user_id=user_id,
            full_name=full_name,
            email=email,
            phone=phone,
            employee_id=employee_id,
            designation_id=designation_id,
            profile_image=profile_image
        )

        return redirect('employee_listing')

    return render(request, 'hr_dashboard/employees/add_employee_detail.html', {
        'users': users,
        'designations': Designation.objects.all()  # send designations for dropdown
    })



@login_required
def employee_profile(request, user_id):
    if request.user.role != 'hr' and request.user.id != int(user_id):
        return HttpResponse("Unauthorized", status=403)

    try:
        profile = EmployeeProfile.objects.get(user_id=user_id)
    except EmployeeProfile.DoesNotExist:
        return HttpResponse("Profile not found", status=404)

    return render(request, 'hr_dashboard/employees/employee_profile.html', {
        'profile': profile
    })