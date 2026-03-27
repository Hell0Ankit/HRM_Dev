from django.urls import path
from attendance import views

urlpatterns = [
    # single employee attendance status 
    path('attendance/', views.attendance, name='attendance'),
    path('attendance_status/', views.attendance_status, name='attendance_status'),

    # All Employee status
    path('all_attendance_status/', views.all_attendance_status, name='all_attendance_status'),

]


