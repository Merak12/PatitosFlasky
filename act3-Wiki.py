import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/The_Umbrella_Academy_(TV_series)"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="mw-content-ltr mw-parser-output")
episodesTables = results.find_all("table", class_="wikitable plainrowheaders wikiepisodetable")

for episodeTable in episodesTables:
    episodeRows = episodeTable.find_all("tr", class_="vevent module-episode-list-row")
    for episode in episodeRows:
        episodeNumber = episode.find("th", scope="row")
        episodeTitle = episode.find("td", class_="summary")
        episodeInfo = episode.find_all("td", style="text-align:center")
        episodeInSeason = episodeInfo[0]
        episodeDirector = episodeInfo[1]
        episodeWriter = episodeInfo[2]
        episodeRelease = episodeInfo[3]
        print("Episode Number: "+episodeNumber.text.strip())
        print("Episode Title: "+episodeTitle.text.strip())
        print("Episode Number in Season: ", episodeInSeason.text.strip())
        print("Episode Director: ", episodeDirector.text.strip())
        print("Episode Writer: ", episodeWriter.text.strip())
        print("Episode Release Date: ", episodeRelease.text.strip())
        print()
