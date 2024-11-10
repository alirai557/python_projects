import requests
import os
from datetime import datetime

# Make sure to have the API key stored in your environment variables
user_api = os.environ.get("current_weather_data")
location = input("Enter the city name: ")

# Define the API endpoint and construct the complete URL with the location and API key
base_url = "https://api.openweathermap.org/data/2.5/weather?q="
complete_api_link = f"{base_url}{location}&appid={user_api}"

# Make a GET request to the API
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# Check if the API returned a valid response for the city
if api_data['cod'] == '404':
    print(f"Invalid City: {location}, please check your city name")
else:
    # Extract and convert the temperature from Kelvin to Celsius
    temp_city = api_data['main']['temp'] - 273.15
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    # Display weather information
    print("------------------------------")
    print(f"Weather Stats for - {location.upper()} || {date_time}")
    print("------------------------------")
    print(f"Current temperature is: {temp_city:.2f}°C")
    print(f"Current weather description: {weather_desc}")
    print(f"Current Humidity: {hmdt}%")
    print(f"Current wind speed: {wind_spd} km/h")