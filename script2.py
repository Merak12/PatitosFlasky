# Escribe un script en python que consulte la API de los perros y que muestre en la pantalla la url de 3 imágenes de perros
import requests

for i in range(3):
    url_endpoint = f"https://api.thedogapi.com/v1/breeds/{i+1}"
    url_images = "https://api.thedogapi.com/v1/images/"
    response_endpoint = requests.get(url_endpoint)
    imageID1 = response_endpoint.json()["reference_image_id"]
    urlSearch = requests.get(url_images + imageID1).json()
    print(urlSearch["url"])

