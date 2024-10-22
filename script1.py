import requests

url = "https://randomuser.me/api/"
query_params = {"nat": "US"}

for i in range (3):
    response = requests.get(url, params=query_params).json()
    print(response)
