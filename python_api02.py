# Random user generator es una herramienta para generar datos aleatorios de usuarios
# https://randomuser.me/api/
# Para obtener la información devuelta se usa el método text
import requests

url = "https://randomuser.me/api/"
response = requests.get(url)

print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)
print(response.text)

