API="http://library.demo.local/api/v1/books"
TOKEN="cisco|NBpQLJK-FqnXOCK2qZwO_7Y3qH2up-s6niuVEkknJlk"

curl -i -X GET "$API" \
  -H "X-API-Key: $TOKEN"
