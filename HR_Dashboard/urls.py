from django.urls import path
from HR_Dashboard import views

urlpatterns = [
    path('', views.hr_dashboard, name='hr_dashboard'),
    path('employee_listing/',views.employee_listing, name='employee_listing' ),
    path('employee_details/',views.employee_details, name='employee_details' ),
    path('add_employee/',views.add_employee, name='add_employee' ),
    path('designations/',views.designations, name='designations' ),
    path('attendance_status/',views.attendance_status, name='attendance_status' ),
    path('leaves_status/',views.leaves_status, name='leaves_status' ),
    path('holydays_listing/',views.holydays_listing, name='holydays_listing' ),
    # path('create_employee/', views.create_employee, name='create_employee'),

]


