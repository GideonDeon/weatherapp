from django.urls import path 
from .views import weather_app, index 

urlpatterns = [
  path('', index, name="index"),
  path('weather_app/', weather_app, name="weatherapp")

]