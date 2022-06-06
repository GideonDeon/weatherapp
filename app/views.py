from ast import Pass
from django.contrib import messages
from django.shortcuts import redirect, render
import json
import urllib.request
import math

def index(request):
    return render(request, "app/index.html",{})

def weather_app(request):
    if  request.POST['location'] == '':
        messages.warning(request, 'Nothing To Geocode')
        return redirect('index')

        
    if request.method == "POST":
        location = request.POST['location']
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=28df930994941ed22e46b0a6355f4ede&units=metric'
        #replacing white spaces
        url2 = url.replace(" ","%20")
        res = urllib.request.urlopen(url2).read()
        json_data = json.loads(res)
        data={
            "city":str(json_data['name']),
            "city_code":str(json_data['sys']['country']),
            #coberting temp and feels_like from floats to integers
            "temp":str(math.floor(json_data['main']['temp'])),
            "feels_like":str(math.floor(json_data['main']['feels_like'])),
            "pressure":str(json_data['main']['pressure']) +'hPa',
            "humidity":str(json_data['main']['humidity'])+'%',
            #converting visibility unit from meters to kilometers
            "visibility":str(math.floor(json_data['visibility']/1000))+'km',
            "wind":str(json_data['wind']['speed'])+'m/s',
            "wind_deg":str(json_data['wind']['deg']),
            "weather":str(json_data['weather'][0]['main']),
            "weather_desc":str(json_data['weather'][0]['description']),
            "weather_icon":str(json_data['weather'][0]['icon']),
            "clouds":str(json_data['clouds']['all'])+'%',
            #covertin lat and lon from floats  to integers
            "lat":str(round(json_data['coord']['lat'],2)),
            "lon":str(round(json_data['coord']['lon'],2)), 
            "cod":json_data['cod'],   
        } 
    else:
        data = {}
    return render(request, 'app/weather_app.html', data)
