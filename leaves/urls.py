from django.urls import path
from leaves import views


urlpatterns = [
    path('leaves/',views.leaves, name='leaves' ),
    path('holidays/',views.holidays, name='holidays' ),
    path('leaves_application/',views.leaves_application, name='leaves_application' ),
]


