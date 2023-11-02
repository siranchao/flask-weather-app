from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_weather(city = "Toronto"):
    url = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"
    weather_data = requests.get(url).json()
    return weather_data


if __name__ == "__main__":
    print("\n*** Get Weather Forecast ***\n")
    city = input("\nEnter a city: ")

    #check user inputs
    if not bool(city.strip()):
        city = "Toronto" 

    weather_data = get_weather(city)
    print(f"\nWeather forecast for {city}:")
    pprint(weather_data)