import requests

from dotenv import load_dotenv
import os 

load_dotenv()

# get api_key 
api_key = os.environ.get("weather_api_key")

# define function to get weather data
def get_current_weather_C(city):
    """Useful for getting weather for a city in °C (celsius)"""

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    #print(data)
    return f"The current temperature in {city} is {data['current']['temp_c']}°C"

def get_current_weather_F(city):
    """Useful for getting weather for a city in °F (Fahrenheit)"""

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    #print(data)
    return f"The current temperature in {city} is {data['current']['temp_f']}°F"
