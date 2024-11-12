import requests
from datetime import datetime

# API key from OpenWeatherMap
API_KEY = "d7743a5b796a220963fceab06d718ef7"  

def get_weather(city):
    # URL to get weather data from OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    # Sending a request to the API
    response = requests.get(url)
    
    # If the response status code is 200 (OK)
    if response.status_code == 200:
        data = response.json()  
        
        # Extracting required information
        city_name = data['name']
        country = data['sys']['country']
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15  # Convert temperature to Celsius
        weather_desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Get the current date and time
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        # Display the weather report
        print(f"Weather Report for {city_name}, {country}")
        print(f"Date & Time: {date_time}")
        print(f"Temperature: {temp_celsius:.2f}°C")
        print(f"Weather: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found, please check the name and try again.")


city = input("Enter the city name: ")
get_weather(city)