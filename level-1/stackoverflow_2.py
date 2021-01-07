from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Pregunta(Item):
  id = Field()
  pregunta = Field()
  # descripcion = Field()


class StackOverflowSpider(Spider):
  name = "MiPrimerSpider"
  custom_settings = {
    "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
  }

  start_urls = ["https://stackoverflow.com/questions"]

  def parse(self, response):
    sel = Selector(response)
    preguntas = sel.xpath('//div[@id="questions"]//div[@class="question-summary"]')
    for pregunta in preguntas: 
      item = ItemLoader(Pregunta(), pregunta)
      item.add_xpath('pregunta', './/h3/a/text()')
      # item.add_xpath('descripcion', './/div[@class="excerpt"]/text()')
      item.add_value('id', 1)

      yield item.load_item()

#scrapy runspider stackoverflow_2.py -o video.csv -t csv <- terminal
