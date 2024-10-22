# Con la finalidad de acceder exclusivamente al listado de trabajos, se puede acceder
# a través de la clase card-content identificados por elementos <div>
# Esto permite acceder al listado de trabajos, pero aún con mucho código html alrededor
# El siguiente ejemplo separa cada componente de cada trabajo usando <h2> para el título,
# <h3> para la compañía y <p> para la ubicación
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    print(job_element, end="\n"*2)
