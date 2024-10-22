# Se demuestra la localización del id="ResultsContainer" con el fin de listar todos los puestos
# de trabajo publicados
# El resultado aún contiene la estructura de la página
# La página en cuestión tiene la siguiente estructura
"""
<div id="ResultsContainer">
  <!-- all the job listings -->
</div>
"""

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())