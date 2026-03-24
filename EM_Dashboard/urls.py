from django.urls import path
from EM_Dashboard import views

urlpatterns = [
    path('employee-dashboard/', views.em_dashboard, name='em_dashboard'),
    path('personal_details/',views.personal_details , name='personal_details' ),
    path('my_attendance/',views.my_attendance , name='my_attendance' ),
    path('leaves_application/',views.leaves_application, name='leaves_application' ),
    path('em_leaves_status/',views.em_leaves_status, name='em_leaves_status' ),
    path('em_holydays_listing/',views.em_holydays_listing, name='em_holydays_listing' ),

]


