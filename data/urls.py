from django.urls import path 
from .views import *

app_name = 'data'

urlpatterns = [
    path('weather/', currentWeather, name="current-weather")
]

'''
    weather?
    hourly?
    daily?
'''