from django.urls import path
from attendance import views


urlpatterns = [
    path('attendance/',views.attendance, name='attendance' ),
    path('holidays/',views.holidays, name='holidays' ),
]


