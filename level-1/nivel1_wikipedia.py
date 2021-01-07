import requests
from lxml import html

encabezados = {
  "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

#url semilla
url = "https://www.wikipedia.org/"

respuesta = requests.get(url, headers=encabezados)

parser = html.fromstring(respuesta.text)

#html
ingles = parser.get_element_by_id("js-link-box-en")
print(ingles.text_content())

#xpath
ingles2 = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
print(ingles2)

#todos
idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")
for idioma in idiomas: 
  print(idioma)