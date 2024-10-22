# Escribe un script en python que consulte la API de los perros y que muestre en la pantalla la url de 3 imágenes de perros
import requests


url_endpoint1 = "https://api.thedogapi.com/v1/breeds/1"
response_endpoint1 = requests.get(url_endpoint1)

url_endpoint2 = "https://api.thedogapi.com/v1/breeds/2"
response_endpoint2 = requests.get(url_endpoint2)

url_endpoint3 = "https://api.thedogapi.com/v1/breeds/3"
response_endpoint3 = requests.get(url_endpoint3)

print(url_endpoint1)
print(response_endpoint1.json()["reference_image_id"])
print("")
print(url_endpoint2)
print(response_endpoint2.json()["reference_image_id"])
print("")
print(url_endpoint3)
print(response_endpoint3.json()["reference_image_id"])
print("")
