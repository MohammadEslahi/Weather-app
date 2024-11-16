from django.shortcuts import render
import requests



def home(request):
    city = ''
    temperature = None
    weather = None
    error = None

    if request.method =='POST':
        city = request.POST.get('city')
        api_key = ''
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        return render(request, 'home.html', {'data':data})
    else:
        return render(request, 'home.html')