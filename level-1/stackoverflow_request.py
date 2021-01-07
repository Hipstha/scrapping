import requests
from bs4 import BeautifulSoup

headers = {
  "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

url = "https://stackoverflow.com/questions"

respuesta = requests.get(url, headers=headers)

soup = BeautifulSoup(respuesta.text, features="lxml")

#devuelve 1
contenedor_de_preguntas = soup.find("div",id="questions")
#devuelve todo
lista_de_preguntas = contenedor_de_preguntas.find_all("div", class_="question-summary")

for pregunta in lista_de_preguntas:
  # texto_pregunta = pregunta.find("h3").text
  elemento_texto_pregunta = pregunta.find("h3")
  texto_pregunta = elemento_texto_pregunta.text

  descripcion_pregunta = elemento_texto_pregunta.find_next_sibling('div').text

  # descripcion_pregunta = pregunta.find(class_='excerpt').text
  descripcion_pregunta = descripcion_pregunta.replace("\n", "").replace("\r", "").strip()
  print(texto_pregunta)
  print(descripcion_pregunta)

  print()