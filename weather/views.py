from django.shortcuts import render
import requests



def home(request):
    city = ''
    temperature = None
    weather = None
    error = None

    if request.method =='POST':
        city = request.POST.get('city')
        api_key = '05f3869f87eb5393b6a5b843900757d6'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()

        context = {
            'city' : request.POST.get('city'),
            'weather' : data['weather'][0]['description'],
            'temperature': data['main']['temp'] - 273.15,
        }

        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')