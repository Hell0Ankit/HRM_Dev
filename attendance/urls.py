from django.urls import path
from attendance import views


urlpatterns = [
    path('attendance/',views.attendance, name='attendance' ),
    path('leave/',views.leave, name='leave' ),
    path('holidays/',views.holidays, name='holidays' ),
]


