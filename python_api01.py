# Random user generator es una herramienta para generar datos aleatorios de usuarios
# https://randomuser.me/api/
# Response es 200, indicando Your request was successful!
import requests

url = "https://randomuser.me/api/"
r = requests.get(url)

print(r)

