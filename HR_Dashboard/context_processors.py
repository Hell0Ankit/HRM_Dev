from HR_Dashboard.models import Designation

from .models import EmployeeProfile

def designations_data(request):
    return {
        "designations": Designation.objects.all()
    }




