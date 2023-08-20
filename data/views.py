from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from datetime import datetime, timedelta
from .serializers import *
from django.db.models import Q

def getCity(request):
    '''
    helper function to retrive the city in question based on either its name or coordinates
    '''
    location = request.GET.get('city', None)

    if location:
        location = location.title()
        city = City.objects.get(name=location)
    else:
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        city = City.objects.get(lat=lat, lon=lon)
    return city

@api_view(['GET'])
def currentWeather(request):
    city = getCity(request)

    weatherInstances = Weather.objects.filter(city=city)
    cT = datetime.now()

    if cT.minute != 0:
        cT = datetime(year=cT.year, month=cT.month,
                               day=cT.day, hour=cT.hour, minute=0)

    instance = weatherInstances.get(dt=cT)
    serializer = WeatherSerializer(instance)
    return Response(data=serializer.data)

@api_view(['GET'])
def hourly(request):
    city = getCity(request)
    
    weatherInstances = Weather.objects.filter(city=city)
    start = datetime.now()

    if start.minute != 0:
        start = datetime(year=start.year, month=start.month,
                               day=start.day, hour=start.hour, minute=0)
        
    end = start + timedelta(hours=96)
    lookup = Q(dt__lt=start) | Q(dt__gt=end)
    instances = weatherInstances.exclude(lookup)
    serializer = WeatherSerializer(instances, many=True)
    return Response(data=serializer.data)
