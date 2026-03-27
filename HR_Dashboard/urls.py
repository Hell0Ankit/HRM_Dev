from django.urls import path
from HR_Dashboard import views

urlpatterns = [
    path('', views.hr_dashboard, name='hr_dashboard'),
    path('employee_listing/',views.employee_listing, name='employee_listing' ),
    path('employee_details/<int:user_id>/',views.employee_details, name='employee_details' ),
    path('edit_personal_detail/<int:id>/', views.edit_personal_detail, name='edit_personal_detail'),
    path('edit_emergency_contact/<int:id>/', views.edit_emergency_contact, name='edit_emergency_contact'),
    path('edit_bank_account/<int:id>/', views.edit_bank_account, name='edit_bank_account'),
    path('add_employee_detail/',views.add_employee_detail, name='add_employee_detail' ),

    path('designations/',views.designations, name='designations' ),
    path('add_designations/',views.add_designations, name='add_designations' ),
    path('edit_designations/<int:id>/',views.edit_designations, name='edit_designations' ),
    path('delete-designation/<int:id>/', views.delete_designation, name='delete_designation'),
    

    path('leaves_status/',views.leaves_status, name='leaves_status' ),
    path('leave/approve/<int:id>/', views.approve_leave, name='approve_leave'),
    path('leave/reject/<int:id>/', views.reject_leave, name='reject_leave'),

    path('holidays_listing/',views.holidays_listing, name='holidays_listing' ),
    path('add_holiday/',views.add_holiday, name='add_holiday' ),
    path('edit_holiday/<int:id>/',views.edit_holiday, name='edit_holiday' ),

    # 404 error page 
    path('error/',views.error, name='error' ),
]


