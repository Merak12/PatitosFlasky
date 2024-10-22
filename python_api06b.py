# Se demuestra el uso de parámetros en una query
import requests

url = "https://randomuser.me/api/"
query_params = {"gender": "male", "nat": "mx", "state": "hidalgo"}

response = requests.get(url, params=query_params).json()

print(response)