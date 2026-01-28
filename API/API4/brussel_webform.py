#!/usr/bin/env python3
import requests

# Test API die webforms accepteert
URL = "https://httpbin.org/post"

def main():
    # Webform data (zoals uit een HTML form)
    form_data = {
        "city": "Brussel",
        "latitude": "50.85",
        "longitude": "4.35",
        "request": "current_weather"
    }

    response = requests.post(URL, data=form_data, timeout=10)
    response.raise_for_status()

    result = response.json()

    print("== Weather Webform API experiment ==")

    print("\nVerzonden webform data:")
    for key, value in form_data.items():
        print(f"- {key}: {value}")

    print("\nOntvangen door server (form):")
    for key, value in result["form"].items():
        print(f"- {key}: {value}")

if __name__ == "__main__":
    main()
