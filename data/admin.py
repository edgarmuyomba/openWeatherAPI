from django.contrib import admin
from .models import * 

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass 

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ["city", "condition"]
