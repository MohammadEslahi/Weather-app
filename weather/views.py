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
        # second parameter defines the default option
        unit = request.POST.get('unit', 'C')
        city = request.POST.get('city')
        api_key = os.getenv('WeatherAPI-key')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        print(unit)
        
        if data.get("cod") == 200:
            if unit == 'C':
                temperature = round(data['main']['temp'] - 273.15) # rounds it to the nearest whole number
                unit_symbol = 'C'
            else:
                temperature = round((data['main']['temp'] - 273.15)*1.8 +32) # converts to F
                unit_symbol = 'F'
            context = {
                'data': data,
                'city' : request.POST.get('city'),
                'weather' : data['weather'][0]['description'],
                'temperature': temperature,
                'unit': unit,
                'unit_symbol' : unit_symbol,
            }

            return render(request, 'home.html', context)
        else:
            return render(request, 'home.html', {'error':"Haven't heard of ", 'city':city})
    else:
        return render(request, 'home.html')