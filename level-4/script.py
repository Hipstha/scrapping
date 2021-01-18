import requests
from lxml import html
import json

headers = {
  'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
}

respuesta = requests.get('https://www.gob.pe/busquedas?reason=sheet&sheet=1', headers=headers)
respuesta.encoding = 'UTF-8'

parser = html.fromstring(respuesta.text)

datos = parser.xpath('//script[contains(text(), "window.initialData")]')[0].text_content()

indice_initial = datos.find('{')

datos = datos[indice_initial:]

# print(datos)
objeto = json.loads(datos)

resultados = objeto["data"]["attributes"]["results"]

for resultado in resultados:
  if resultado:
    print(resultado["content"])




