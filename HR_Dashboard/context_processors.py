from HR_Dashboard.models import Designation
from .models import EmployeeProfile

def designations_data(request):
    return {
        "designations": Designation.objects.all()
    }

def profile_data(request):
    if not request.user.is_authenticated:
        return {'profile_data': None}
    profile_data = None
    if request.user.role == 'employee':
        try:
            profile = EmployeeProfile.objects.select_related('designation').get(user=request.user)
            profile_data = {
                'full_name': profile.full_name,
                'designation': profile.designation.designation if profile.designation else '',
                'profile_image': profile.profile_image.url if profile.profile_image else None
            }
        except EmployeeProfile.DoesNotExist:
            profile_data = {
                'full_name': request.user.username,
                'designation': '',
                'profile_image': None
            }
    elif request.user.role == 'hr':
        profile_data = {
            'full_name': request.user.username,
            'designation': 'HR',
            'profile_image': None
        }
    return {'profile_data': profile_data}



