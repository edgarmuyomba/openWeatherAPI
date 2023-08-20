from django.urls import path 
from .views import *

app_name = 'data'

urlpatterns = [
    path('weather/', currentWeather, name="current-weather"),
    path('hourly/', hourly, name="96-hours"),
    path('daily/', daily, name="3-days"),
]

'''
    daily?
'''