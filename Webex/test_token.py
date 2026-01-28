import requests
from auth import HEADERS

url = "https://api.ciscospark.com/v1/people/me"

response = requests.get(url, headers=HEADERS)

print("Status code:", response.status_code)
print(response.json())
