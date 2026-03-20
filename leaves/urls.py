from django.urls import path
from leaves import views


urlpatterns = [
   path('leave_applications/',views.leave_applications, name='leave_applications' ),
]


