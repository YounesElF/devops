import requests
from auth import HEADERS

rooms_url = "https://api.ciscospark.com/v1/rooms"
memberships_url = "https://api.ciscospark.com/v1/memberships"

groups_struc = {
    "groups": [
        {
            "group": {
                "group_name": "GROUP_MICRO",
                "members": [
                    {"email": "nick@biasc.be"},
                    {"email": "marcus@biasc.be"}
                ]
            }
        },
        {
            "group": {
                "group_name": "GROUP_NANO",
                "members": [
                    {"email": "alice@biasc.be"}
                ]
            }
        }
    ]
}

rooms = requests.get(rooms_url, headers=HEADERS).json()["items"]

for rec in groups_struc["groups"]:
    group_name = rec["group"]["group_name"]

    room = next((r for r in rooms if r["title"] == group_name), None)
    if not room:
        print(f"Room {group_name} not found")
        continue

    print(f"\nAdding members to {group_name}")

    for member in rec["group"]["members"]:
        payload = {
            "roomId": room["id"],
            "personEmail": member["email"]
        }

        response = requests.post(memberships_url, headers=HEADERS, json=payload)

        if response.status_code >= 300:
            print(f"Failed: {member['email']}")
        else:
            print(f"Added: {member['email']}")
