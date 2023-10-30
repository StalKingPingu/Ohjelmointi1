import requests
import json

location = input('Anna paikkakunta')

api = "ab204412f2e73483f661c77221f72115"

location = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api}"

search = requests.get(location).json()


lon = search[0]['lon']
lat = search[0]['lat']

weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"

currentweather = requests.get(weather).json()
print(currentweather['weather'][0]['main'])
print(currentweather['main']['temp'] -273)