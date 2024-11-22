from django.shortcuts import render
import requests
# instead of hardcoding API-key
import os
from dotenv import load_dotenv
from accounts.models import *

load_dotenv()

def home(request):
    city = ''
    temperature = None
    weather = None
    error = None

    if request.method =='POST':

        # adding favorite cities (checks name of html button)
        if 'Add city to fav' in request.POST:
            searched_city = request.POST.get('city') # city that user has searched.
            City.objects.get_or_create(name=searched_city)
            request.user.fav_cities.add(City.objects.get(name=searched_city))
            print(request.user.fav_cities.all())
            
            

        # second parameter defines the default option
        unit = request.POST.get('unit', 'C')
        city = request.POST.get('city')
        api_key = os.getenv('WeatherAPI-key')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()

        if not api_key:
            return render(request,'home.html', {'error':"API-key not provided, you may need to add one."})
        
        elif not city:
            return render(request,'home.html',{'error':"We won't know where to look for, if you haven't written a city name :)"})
        
        else:
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
                return render(request, 'home.html', {'error':"We looked every single corner, but couldn't find ", 'city':city or ''})
    else:
        return render(request, 'home.html', {'city':city or '','error':error})