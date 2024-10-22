# Se accede a una página falsa de anuncio de trabajos
# El contenido es estático
# El resultado del script es el contenido que se puede obtener con Inspector

import requests

URL = "https://toposfc.org/"
page = requests.get(URL)

print(page.text)