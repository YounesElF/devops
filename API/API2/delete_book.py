import os
import requests

APIHOST = "http://library.demo.local"

def get_token() -> str:
    token = os.getenv("LIBRARY_TOKEN", "").strip()
    if not token:
        raise Exception("LIBRARY_TOKEN is not set (export it in your terminal)")
    return token

def delete_book(book_id: int):
    token = get_token()

    r = requests.delete(
        f"{APIHOST}/api/v1/books/{book_id}",
        headers={"X-API-Key": token},
        timeout=10
    )

    print("Status:", r.status_code)
    # Sommige APIs geven 200 met JSON, andere 204 zonder body
    if r.text.strip():
        try:
            print(r.json())
        except Exception:
            print(r.text)
    else:
        print(f"Book {book_id} deleted (no content).")

if __name__ == "__main__":
    delete_book(101)   # pas aan naar bestaand id

