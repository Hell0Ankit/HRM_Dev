from django.urls import path
from employees import views


urlpatterns = [
   path('employee_listing/',views.employee_listing, name='employee_listing' )
]


