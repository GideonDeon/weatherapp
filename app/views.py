from ast import Pass
from django.shortcuts import render
import json
import urllib.request
from datetime import datetime
import math

def index(request):
    return render(request, "app/index.html",{})

def weather_app(request):
    if request.method == "POST":
        location = request.POST['location']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=28df930994941ed22e46b0a6355f4ede&units=metric').read()
        geo = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=28df930994941ed22e46b0a6355f4ede').read()
        json_data = json.loads(res)
        json_geo = json.loads(geo)
        data={
            "city":str(json_data['name']),
            "city_code":str(json_data['sys']['country']),
            "temp":str(math.floor(json_data['main']['temp'])),
            "feels_like":str(math.floor(json_data['main']['feels_like'])),
            "pressure":str(json_data['main']['pressure']) +'hPa',
            "humidity":str(json_data['main']['humidity'])+'%',
            "visibility":str(math.floor(json_data['visibility']/1000))+'km',
            "wind":str(json_data['wind']['speed'])+'m/s',
            "wind_deg":str(json_data['wind']['deg']),
            "weather":str(json_data['weather'][0]['main']),
            "weather_desc":str(json_data['weather'][0]['description']),
            "weather_icon":str(json_data['weather'][0]['icon']),
            "clouds":str(json_data['clouds']['all'])+'%',
            "lat":str(round(json_data['coord']['lat'],2)),
            "lon":str(round(json_data['coord']['lon'],2)),    
        }
    else:
        data = {}
    return render(request, 'app/weather_app.html', data)
