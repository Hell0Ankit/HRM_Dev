from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),  
    path('change_password/', views.change_password, name='change_password'),  
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),


    # this class only showing utilities items 
    path('', views.utilities, name='utilities'),  

]


