import requests
from auth import HEADERS

rooms_url = "https://api.ciscospark.com/v1/rooms"

rooms = requests.get(rooms_url, headers=HEADERS).json()["items"]

print("Groupen_:\n")

for room in rooms:
    if "GROUP_" in room["title"]:
        print("-", room["title"])
