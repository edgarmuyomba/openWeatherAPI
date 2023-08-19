from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from datetime import datetime
from .serializers import *


@api_view(['GET'])
def currentWeather(request):
    location = request.GET.get('city', None)

    if location:
        location = location.title()
        city = City.objects.get(name=location)
    else:
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        city = City.objects.get(lat=lat, lon=lon)

    weatherInstances = Weather.objects.filter(city=city)
    cT = datetime.now()

    if cT.minute != 0:
        currentTime = datetime(year=cT.year, month=cT.month,
                               day=cT.day, hour=cT.hour, minute=0)

    instance = weatherInstances.get(dt=currentTime)
    serializer = WeatherSerializer(instance)
    return Response(data=serializer.data)
