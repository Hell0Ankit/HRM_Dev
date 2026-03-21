from django.urls import path
from employees import views


urlpatterns = [
   path('employee_listing/',views.employee_listing, name='employee_listing' ),
   path('employee_profile/',views.employee_profile, name='employee_profile' ),
   path('add_employees/',views.add_employees, name='add_employees' ),
   path('designations/',views.designations, name='designations' ),
   # for employee  
   path('personal_details/',views.personal_details , name='personal_details' ),


]


