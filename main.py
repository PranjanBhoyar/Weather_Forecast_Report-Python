import requests
from pprint import pprint

API_KEY = '842d19373c3c6038a84bd1cb4be08f78'
city = input("Enter the name of city: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?q=Nagpur,in&appid=" + API_KEY
weather_data = requests.get(base_url).json()
pprint(weather_data)
