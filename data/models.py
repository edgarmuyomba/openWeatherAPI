from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=5, decimal_places=2)
    lon = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cities"

class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    dt = models.DateTimeField()
    condition = models.CharField(max_length=50)
    temp = models.IntegerField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()

    class Meta:
        ordering = ['dt']
        verbose_name_plural = "Weather"