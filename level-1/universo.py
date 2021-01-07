from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

from scrapy.crawler import CrawlerProcess

class Noticia(Item):
  titular = Field()
  descripcion = Field()

class ElUniversoSpider(Spider):
  name = "MiSegundoSpider"
  custom_settings = {
    "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
  }

  start_urls = ['https://www.eluniverso.com/deportes']

  def parse(self, response):
    # sel = Selector(response)
    # noticias = sel.xpath('//div[@class="view-content"]/div[@class="posts"]')
    # for noticia in noticias:
    #   item = ItemLoader(Noticia(), noticia)
    #   item.add_xpath('titular', './/h2/a/text()')
    #   item.add_xpath('descripcion', './/p/text()')

    #   yield item.load_item()

    soup = BeautifulSoup(response.body, features="lxml")
    contenedor_noticias = soup.find_all('div', class_='view-content')

    for contenedor in contenedor_noticias:
      noticias = contenedor.find_all('div', class_='posts', recursive=False)
      for noticia in noticias:
        item = ItemLoader(Noticia(), response.body)

        titular = noticia.find('h2').text
        descripcion = noticia.find('p')

        if (descripcion != None):
          descripcion = descripcion.text
        else:
          descripcion = 'N/A'

        item.add_value('titular', titular)
        item.add_value('descripcion', descripcion)

        yield item.load_item()

#Ejecucion
process = CrawlerProcess({
  'FEED_FORMAT': 'csv',
  'FEED_URI': 'resultados.csv'
})

process.crawl(ElUniversoSpider)
process.start()