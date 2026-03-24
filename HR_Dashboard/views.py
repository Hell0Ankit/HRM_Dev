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
        profile_image = request.FILES.get('profile_image')
        full_name = request.POST.get('full_name')
        employee_id = request.POST.get('employee_id')
        designation_id = request.POST.get('designation')
        joining_date= request.FILES.get('joining_date')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        primary_name = request.POST.get('primary_name')
        primary_relation = request.POST.get('primary_relation')
        primary_phone = request.POST.get('primary_phone')
        primary_email = request.POST.get('primary_email')
        primary_address = request.POST.get('primary_address')

        secondary_name = request.POST.get('secondary_name')
        secondary_relation = request.POST.get('secondary_relation')
        secondary_phone = request.POST.get('secondary_phone')
        secondary_email = request.POST.get('secondary_email')
        secondary_address = request.POST.get('secondary_address')

        account_holder = request.POST.get('account_holder')
        account_number = request.POST.get('account_number')
        bank_name = request.POST.get('bank_name')
        branch_name = request.POST.get('branch_name')
        ifsc_code = request.POST.get('ifsc_code')

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
            profile_image=profile_image,
            joining_date=joining_date,
            birthday=birthday,
            gender=gender,
            address=address,
            primary_name=primary_name,
            primary_relation=primary_relation,
            primary_phone=primary_phone,
            primary_email=primary_email,
            primary_address=primary_address,

            secondary_name=secondary_name,
            secondary_relation=secondary_relation,
            secondary_phone=secondary_phone,
            secondary_email=secondary_email,
            secondary_address=secondary_address,
            account_holder=account_holder,
            account_number=account_number,
            bank_name=bank_name,
            branch_name=branch_name,
            ifsc_code=ifsc_code

        )

        return redirect('employee_listing')

    return render(request, 'hr_dashboard/employees/add_employee_detail.html', {
        'users': users,
        'designations': Designation.objects.all()  # send designations for dropdown
    })



@login_required
def employee_details(request, user_id):
    if request.user.role != 'hr' and request.user.id != int(user_id):
        return HttpResponse("Unauthorized", status=403)

    try:
        profile = EmployeeProfile.objects.get(user_id=user_id)
    except EmployeeProfile.DoesNotExist:
        return HttpResponse("Profile not found", status=404)
    return render(request, 'hr_dashboard/employees/employee_details.html',{
        'profile': profile
    })


    
    
