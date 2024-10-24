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

URLHoyts = "https://www.hoyts.com.au/movies/coming-soon"
hoytsBillboard = requests.get(URLHoyts)

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
    print(f"Movie Title: {movie_title_text}, Release Date: {release_date_text}")
print()

print(color.BOLD + "Cartelera de Cinépolis" + color.END)
for article, release_date in zip(upcomingCinepolis, releaseCinepolis):
    movies = article.find_all("li")
    
    for movie in movies:
        movie_title = movie.find("figcaption")
        print(f"Movie Title: {movie_title.text.strip()}, Release Date: {release_date.text.strip()}")