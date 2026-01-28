API="http://library.demo.local/api/v1/books"
TOKEN="cisco|NBpQLJK-FqnXOCK2qZwO_7Y3qH2up-s6niuVEkknJlk"

curl -i -X POST http://library.demo.local/api/v1/books \
  -H "Content-Type: application/json" \
  -H "X-API-Key: cisco|NBpQLJK-FqnXOCK2qZwO_7Y3qH2up-s6niuVEkknJlk" \
  -d '{
    "id": 101,
    "title": "REST API met curl",
    "author": "Younes",
    "isbn": "978-1-23456-789-0"
  }'
