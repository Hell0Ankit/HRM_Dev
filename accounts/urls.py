from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('create_employee/', views.create_employee, name='create_employee'),  
    path('change_password/', views.change_password, name='change_password'),  

    path('redirect/', views.dashboard_redirect, name='dashboard_redirect'),
    path('logout/', views.user_logout, name='logout'),


    # this class only showing utilities items 
    path('', views.utilities, name='utilities'),  

]


