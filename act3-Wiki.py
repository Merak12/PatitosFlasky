import requests
from bs4 import BeautifulSoup
import numpy as np
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

# Extraer 
URL = "https://en.wikipedia.org/wiki/The_Umbrella_Academy_(TV_series)"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="mw-content-ltr mw-parser-output")
episodesTables = results.find_all("table", class_="wikitable plainrowheaders wikiepisodetable")

episode_data = []

for episodeTable in episodesTables:
    episodeRows = episodeTable.find_all("tr", class_="vevent module-episode-list-row")
    for episode in episodeRows:
        episodeNumber = episode.find("th", scope="row").text.strip()
        episodeTitle = episode.find("td", class_="summary").text.strip()
        episodeInfo = episode.find_all("td", style="text-align:center")
        episodeInSeason = episodeInfo[0].text.strip()
        episodeDirector = episodeInfo[1].text.strip()
        episodeWriter = episodeInfo[2].text.strip()
        episodeRelease = episodeInfo[3].text.strip()

        episode_data.append([episodeNumber, episodeTitle, episodeInSeason, episodeDirector, episodeWriter, episodeRelease])

episode_matrix = np.array(episode_data)

class Busqueda(FlaskForm):
    tipo_busqueda = RadioField('Selecciona una opción:', 
                                choices=[('1', 'Número de episodio'), 
                                         ('2', 'Titulo de episodio'), 
                                         ('3', 'Número de episodio por temporada'), 
                                         ('4', 'Director'), 
                                         ('5', 'Escritor'), 
                                         ('6', 'fecha de lanzamiento')],
                                validators=[DataRequired()])  
    palabra_clave = StringField('Ingrese el dato que quiere encontrar:', validators=[DataRequired()])
    submit = SubmitField('Buscar')

def buscar_episodio_por_palabra(clave, category):
    clave = clave.strip().lower()  
    resultados = [episodio for episodio in episode_matrix if clave in episodio[category].strip().lower()]
    return resultados  

@app.route('/activity3pelis', methods=['GET', 'POST'])
def buscar():
    form = Busqueda() 
    resultados = [] 

    if form.validate_on_submit():  
        tipo_busqueda = form.tipo_busqueda.data  
        palabra_clave = form.palabra_clave.data  
        category_index = int(tipo_busqueda) - 1 
        
        resultados = buscar_episodio_por_palabra(palabra_clave, category_index)  
    
    return render_template('activity3pelis.html', form=form, resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)



    
    
