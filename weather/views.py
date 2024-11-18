from django.shortcuts import render
import requests
# instead of hardcoding API-key
import os
from dotenv import load_dotenv

load_dotenv()

def home(request):
    city = ''
    temperature = None
    weather = None
    error = None

    if request.method =='POST':
        city = request.POST.get('city')
        api_key = os.getenv('WeatherAPI-key')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()

        context = {
            'data': data,
            'city' : request.POST.get('city'),
            'weather' : data['weather'][0]['description'],
            'temperature': round(data['main']['temp'] - 273.15), #rounds it to the nearest whole number
        }

        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')