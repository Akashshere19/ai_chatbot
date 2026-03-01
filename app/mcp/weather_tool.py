import requests


def get_weather(city: str) -> str:
    """
    Get current weather for a city
    """

    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo = requests.get(
        geo_url,
        params={"name": city, "count": 1}
    ).json()

    if "results" not in geo:
        return f"City '{city}' not found."

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather = requests.get(
        weather_url,
        params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }
    ).json()

    current = weather["current_weather"]

    return (
        f"Weather in {city}:\n"
        f"Temperature: {current['temperature']}°C\n"
        f"Wind Speed: {current['windspeed']} km/h"
    )