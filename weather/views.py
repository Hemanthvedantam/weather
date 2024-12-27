from django.shortcuts import render,redirect
from .Utils import get_weather_data
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def weather_view(request):
    # Get city from GET request or default to London
    city = request.GET.get('city', 'London')
    weather_data = get_weather_data(city)
    return render(request, 'weather/index.html', {'weather': weather_data, 'city': city})

