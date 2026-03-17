from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),  

    # this class only showing utilities items 
    path('utilities/', views.utilities, name='utilities'),  

]


