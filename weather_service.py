import requests

def fetch_weather(city_name: str, api_key: str) -> dict:
    """
    Fetches real-time weather details for a specific city from the OpenWeather API.
    Returns a dictionary of clean data if successful, or an error message if it fails.
    """
    base_url = "https://openweathermap.org"
    
    # Pack parameters. 'units=metric' returns temperatures in Celsius.
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=5)
        data = response.json()
        
        # OpenWeather returns a 'cod' status code of 200 when a city is found
        if data.get("cod") == 200:
            return {
                "success": True,
                "city": data["name"],
                "country": data["sys"]["country"],
                "temp": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"].title(),
                "wind_speed": data["wind"]["speed"]
            }
        else:
            return {
                "success": False, 
                "message": data.get("message", "City not found.")
            }
            
    except requests.exceptions.RequestException as e:
        return {
            "success": False, 
            "message": f"Connection error: {str(e)}"
        }
