from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.hr_dashboard, name='hr_dashboard'),

]


