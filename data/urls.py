from django.urls import path 
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'data'

urlpatterns = [
    path('weather/', currentWeather, name="current-weather"),
    path('hourly/', hourly, name="96-hours"),
    path('daily/', daily, name="3-days"),
    path('auth/', obtain_auth_token),
]