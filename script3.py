#Escribe un script en python que consulte la API de los casos confirmados de paises y muestre el numero de casos confirmados en méxico al dia de 27 de OCTUBRE de 2021


#Escribe un script en python que consulte la API de los casos confirmados de paises y muestre el numero de casos confirmados en méxico al dia de 27 de OCTUBRE de 2021
import requests

country = 'mexico'
date = '2021-10-27'
api_url = 'https://api.api-ninjas.com/v1/covid19?country={}'.format(country)
response = requests.get(api_url, headers={'X-Api-Key': '2EaZcOXJ0BlavQNp/OCwNQ==FOldfxFGMvcWHEdp'})


response_json = response.json()  

country_data = response_json[0]  

cases = country_data['cases']

date = cases['2021-10-27']

numberOfCases = date['total']

print("El numero de casos confirmasdos es: ", numberOfCases)


