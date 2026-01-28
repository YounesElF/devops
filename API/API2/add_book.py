import os
import requests

APIHOST = "http://library.demo.local"

def get_token() -> str:
    token = os.getenv("LIBRARY_TOKEN", "").strip()
    if not token:
        raise Exception("LIBRARY_TOKEN is not set (export it in your terminal)")
    return token

def add_book(book_id: int):
    token = get_token()
    book = {
        "id": book_id,
        "title": "REST API met Python",
        "author": "Younes",
        "isbn": "978-1-23456-789-0"
    }

    r = requests.post(
        f"{APIHOST}/api/v1/books",
        headers={"X-API-Key": token, "Content-Type": "application/json"},
        json=book,
        timeout=10
    )

    print("Status:", r.status_code)
   
    try:
        print(r.json())
    except Exception:
        print(r.text)

if __name__ == "__main__":
    add_book(101) 

