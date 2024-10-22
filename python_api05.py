# Este ejemplo muestra el formateo de la respuesta usando el método json()
# Esto es posible cuando el Content-type es "application/json"
import requests

url = "https://api.thecatapi.com/v1/breeds/abys"
response = requests.get(url)

#print(response.json())
print(response.json()["description"])
