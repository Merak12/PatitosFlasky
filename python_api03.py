# The Cat API permite obtener las diferentes razas de gatos y sus imágenes
# https://api.thecatapi.com/
# Este ejemplo demuestra el uso de endpoints y URL bases
# Para perros https://api.thedogapi.com/v1/breeds
import requests

url_base = "https://api.thedogapi.com/"
response_base = requests.get(url_base)
#print(response_base.text)

url_endpoint = "https://api.thedogapi.com/v1/breeds"
response_endpoint = requests.get(url_endpoint)
print(response_endpoint.text)