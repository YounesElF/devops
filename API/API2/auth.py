import requests

APIHOST = "http://library.demo.local"

def getAuthToken():
    r = requests.post(
        f"{APIHOST}/api/v1/login",
        json={"username": "admin", "password": "admin"},
        timeout=10
    )
    r.raise_for_status()
    return r.json()["token"]
