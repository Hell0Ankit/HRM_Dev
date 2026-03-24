from HR_Dashboard.models import Designation

def designations_data(request):
    return {
        "designations": Designation.objects.all()
    }