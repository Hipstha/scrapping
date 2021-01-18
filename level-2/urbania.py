from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Departamento(Item):
  nombre = Field()
  direccion = Field()

class Urbaniape(CrawlSpider):
  name = "Departamentos"
  custom_settings = {
    "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "CLOSESPIDER_ITEMCOUNT": 24
  }

  start_urls = [
    'https://urbania.pe/buscar/proyectos-propiedades?page=1',
    'https://urbania.pe/buscar/proyectos-propiedades?page=2',
    'https://urbania.pe/buscar/proyectos-propiedades?page=3',
    'https://urbania.pe/buscar/proyectos-propiedades?page=4',
    'https://urbania.pe/buscar/proyectos-propiedades?page=5',
  ]

  allowed_domains = ['urbania.pe']

  download_delay = 1

  rules = (
    Rule(
      LinkExtractor(
        allow = r'/proyecto-'
      ), follow = True, callback="parse_depa"
    ),
  )

  def parse_depa(self, response):
    sel = Selector(response)
    item = ItemLoader(Departamento(), sel)

    item.add_xpath('nombre', '//h2[@class="info-title"]/text()')
    item.add_xpath('direccion', '//h2[@class="info-location"]/text()')

    yield item.load_item()

