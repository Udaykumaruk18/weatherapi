import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Celsius
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"🌤 Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print(" Failed to retrieve weather data. Please check the city name or API key.")


API_KEY = "7dc6e4149828f811e558584da35a264d"  # Replace with your OpenWeatherMap API key
city_name = input("Enter a city name: ")
get_weather(city_name, API_KEY)