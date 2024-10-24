import requests
from bs4 import BeautifulSoup

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

soupCinepolis = BeautifulSoup(cinepolisBillboard.content, "html.parser")
upcomingCinepolis = soupCinepolis.find_all("div", class_="listProxEstreno cf")

print(color.BOLD + "Cartelera de Hoyts" + color.END)
for movie in moviesHoyts:
    movie_title = movie.find("a", class_="movies-list__link")
    if movie_title:  # Ensure the link exists
        print("Movie Title:",movie_title.text.strip())

print()
print(color.BOLD + "Cartelera de Cinépolis" + color.END)
for article in upcomingCinepolis:
    movies = article.find_all("li")
    
    for movie in movies:
        movie_title = movie.find("figcaption")
        print(f"Movie Title: {movie_title.text.strip()}")
    
    print()
