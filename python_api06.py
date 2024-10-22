# Este ejemplo con respuesta formateada permite saber los parámetros que se entregan
# En la parte b de este ejemplo se muestra cómo se accede a parámetros específicos usando queries
import requests

url = "https://randomuser.me/api/"
response = requests.get(url).json()

print(response)