from rest_framework import serializers
from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'lat', 'lon']

class WeatherSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Weather 
        fields = ['city', 'dt', 'condition', 'temp', 'pressure', 'humidity']