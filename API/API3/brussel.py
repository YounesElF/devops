import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def main():
    params = {
        "latitude": 50.85,
        "longitude": 4.35,
        "current_weather": True
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    weather = data["current_weather"]

    print("== Huidig weer in Brussel ==")
    print(f"Temperatuur : {weather['temperature']} °C")
    print(f"Windsnelheid: {weather['windspeed']} km/h")
    print(f"Windrichting: {weather['winddirection']}°")
    print(f"Tijd        : {weather['time']}")

if __name__ == "__main__":
    main()
