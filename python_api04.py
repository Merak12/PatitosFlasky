# Este ejemplo muestra dos tipos de HTTP headers
# Content-Type	What type of content the server will respond with
# User-Agent	What software the client is using to communicate with the server

import requests

url1 = "https://api.thecatapi.com/v1/breeds/abys"
url2 = "https://api.thecatapi.com/v1/breeds/abys"

response1 = requests.get(url1)
print(response1.headers)

response2 = requests.get(url2)
print(response2.request.headers)