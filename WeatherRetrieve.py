import requests


def geocode_location(location: str):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={location}"
    r = requests.get(url, headers={"User-Agent": "WeatherAppDemo/1.0"})
    r.raise_for_status()
    data = r.json()
    if not data:
        return None
    return {"name": data[0]["display_name"], "lat": data[0]["lat"], "lon": data[0]["lon"]}


# --- 2. Fetch Met Éireann forecast data ---
def fetch_forecast(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&hourly=temperature_2m,precipitation,wind_speed_10m"
        f"&timezone=Europe/Dublin"
    )
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()