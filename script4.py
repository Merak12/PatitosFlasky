#Escribe un script en Python que extraiga la lista de episodios de la serie "Titans" (https://en.wikipedia.org/wiki/Titans_(2018_TV_series)) y los despliegue ne la pantalla de la siguiente forma:

import requests

url = "https://en.wikipedia.org/wiki/Titans_(2018_TV_series)"
response = requests.get(url)

print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)
print(response.text)