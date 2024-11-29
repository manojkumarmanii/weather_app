from django.db import models
from django.contrib.auth.models import User

class CitySearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    search_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} searched {self.city_name} on {self.search_time}"

class WeatherData(models.Model):
    city_name = models.CharField(max_length=100)
    temperature = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    condition = models.CharField(max_length=100)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather for {self.city_name} recorded at {self.recorded_at}"

