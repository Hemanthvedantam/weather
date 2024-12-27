from django.db import models

class WeatherQuery(models.Model):
    city = models.CharField(max_length=100, help_text="Name of the city queried")
    date = models.DateTimeField(auto_now_add=True, help_text="Date and time of the query")
    temperature = models.FloatField(null=True, blank=True, help_text="Temperature in °C")
    condition = models.CharField(max_length=255, null=True, blank=True, help_text="Weather condition description")
    humidity = models.FloatField(null=True, blank=True, help_text="Humidity percentage")
    wind_speed = models.FloatField(null=True, blank=True, help_text="Wind speed in m/s")

    def __str__(self):
        return f"Weather query for {self.city} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

class BackgroundImage(models.Model):
    city = models.CharField(max_length=100, unique=True, help_text="City name for the background image")
    image_url = models.URLField(help_text="URL of the background image")

    def __str__(self):
        return f"Background image for {self.city}"
