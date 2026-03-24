from django.urls import path
from HR_Dashboard import views

urlpatterns = [
    path('hr-dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('employee_listing/',views.employee_listing, name='employee_listing' ),
    path('employee_details/<int:user_id>/',views.employee_details, name='employee_details' ),
    path('add_employee_detail/',views.add_employee_detail, name='add_employee_detail' ),
    path('designations/',views.designations, name='designations' ),
    path('add_designations/',views.add_designations, name='add_designations' ),
    path('edit_designations/<int:id>/',views.edit_designations, name='edit_designations' ),
    path('delete-designation/<int:id>/', views.delete_designation, name='delete_designation'),
    path('attendance_status/',views.attendance_status, name='attendance_status' ),
    path('leaves_status/',views.leaves_status, name='leaves_status' ),
    path('holydays_listing/',views.holydays_listing, name='holydays_listing' ),
    # path('create_employee/', views.create_employee, name='create_employee'),

]


