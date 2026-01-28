import requests
from auth import HEADERS

rooms_url = "https://api.ciscospark.com/v1/rooms"

groups = ["GROUP_MICRO", "GROUP_NANO"]

for group in groups:
    payload = {"title": group}

    response = requests.post(rooms_url, headers=HEADERS, json=payload)

    if response.status_code >= 300:
        print(f"Failed to create {group}")
        print(response.text)
    else:
        print(f"Created {group}")
