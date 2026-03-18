from django.urls import path
from employees import views


urlpatterns = [
   path('employee_listing/',views.employee_listing, name='employee_listing' ),
   path('employee_profile/',views.employee_profile, name='employee_profile' ),
   path('designations/',views.designations, name='designations' ),
]


