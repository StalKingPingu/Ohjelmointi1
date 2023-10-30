import requests
import json

search = "https://api.chucknorris.io/jokes/random"

request = requests.get(search).json()

print(request  ['value'])