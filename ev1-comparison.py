import requests
from bs4 import BeautifulSoup
import numpy as np
import numpy as np
from datetime import datetime
import locale


current_year = datetime.now().year

def convertir_fecha_ahoy(fecha_str):
    fecha_str = str(fecha_str)
    
    try:
        fecha_obj = datetime.strptime(fecha_str, '%d de %B')
        fecha_obj = fecha_obj.replace(year=current_year)
    except ValueError:
        try:
            fecha_obj = datetime.strptime(fecha_str, '%d %b %Y')
        except ValueError:
            return "Formato desconocido"
    
    return fecha_obj.strftime('%Y-%m-%d')


def convertir_fecha_cinepolis(fecha_str):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  

    fecha_str = str(fecha_str)
    
    try:
        fecha_obj = datetime.strptime(fecha_str, '%d de %B')
        fecha_obj = fecha_obj.replace(year=current_year)
    except ValueError:
        try:
            fecha_obj = datetime.strptime(fecha_str, '%d %b %Y')
        except ValueError:
            return "Formato desconocido"
    
    return fecha_obj.strftime('%Y-%m-%d')



movies_info_cinepolis = []
movies_info_ahoy = []

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

URLCinemex = "https://www.hoyts.com.au/movies/coming-soon"
hoytsBillboard = requests.get(URLCinemex)

URLCinepolis = "https://cinepolis.com/proximos-estrenos"
cinepolisBillboard = requests.get(URLCinepolis)

soupHoyts = BeautifulSoup(hoytsBillboard.content, "html.parser")
upcomingHoyts = soupHoyts.find("ul", class_="movies-list")
moviesHoyts = upcomingHoyts.find_all("div", class_="movies-list__wrapper")
releaseHoyts = upcomingHoyts.find_all("span", class_="movies-list__release-date")

soupCinepolis = BeautifulSoup(cinepolisBillboard.content, "html.parser")
upcomingCinepolis = soupCinepolis.find_all("div", class_="listProxEstreno cf")
releaseCinepolis = soupCinepolis.find_all("div", class_="diaEstreno")


for movie in moviesHoyts:
    movie_title = movie.find("a", class_="movies-list__link")
    release_date = movie.find("span", class_="movies-list__release-date")

    if movie_title:
        movie_title_text = movie_title.text.strip()
    else:
        movie_title_text = "Unknown Title"

    if release_date:
        release_date_text = release_date.text.strip()
    else:
        release_date_text = "Release date not available"
    movies_info_ahoy.append([movie_title.text.strip(), release_date.text.strip()])
    

    
print()

for article, release_date in zip(upcomingCinepolis, releaseCinepolis):
    movies = article.find_all("li")
    
    for movie in movies:
        movie_title = movie.find("figcaption")
        movies_info_cinepolis.append([movie_title.text.strip(), release_date.text.strip()])



ahoy = np.array(movies_info_ahoy)
cinepolis = np.array(movies_info_cinepolis)

for i in range(len(ahoy)):
    ahoy[i, 1] = convertir_fecha_ahoy(ahoy[i, 1])  



for i in range(len(cinepolis)):
    cinepolis[i, 1] = convertir_fecha_cinepolis(cinepolis[i, 1])  


print(color.BOLD + "Cartelera de Ahoy" + color.END)

print(ahoy)

print(color.BOLD + "Cartelera de Cinépolis" + color.END)

print(cinepolis)




#de aqui le puedes mover xd


fecha = "2024-10-31"
nombre = "Golpe de Suerte en París"


print("ahoys fechas: ")

for i in range(len(ahoy)):
    if fecha == ahoy[i][1]: #se cambia por 0 para nombre
        print(ahoy[i][0])
        
        
print("cinepolis fechas: ")
for i in range(len(cinepolis)):
    if fecha == cinepolis[i][1]:
        print(cinepolis[i][0])
        
        
print("ahoys nombres: ")

for i in range(len(ahoy)):
    if nombre == ahoy[i][0]: #se cambia por 0 para nombre
        print(ahoy[i][0])
        
        
print("cinepolis nombres: ")
for i in range(len(cinepolis)):
    if nombre == cinepolis[i][0]:
        print(cinepolis[i][0])
        
print("borrar esto")
        



        