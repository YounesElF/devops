import requests
import os

APIHOST = "http://library.demo.local"
token = os.getenv("LIBRARY_TOKEN", "").strip()

if not token:
    raise Exception("LIBRARY_TOKEN is not set")

r = requests.get(
    f"{APIHOST}/api/v1/books",
    headers={"X-API-Key": token},
    timeout=10
)

print("Status:", r.status_code)
print(r.json())

