import requests
from django.conf import settings

def get_weather_data(city):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.WEATHER_API_KEY}&units=metric"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return None
