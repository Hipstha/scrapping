from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Farmacia(Item):
  Nombre = Field()
  Precio = Field()

class CruzVerde(CrawlSpider):
  name = 'Farmacias'

  custom_settings = {
    "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
  }

  allowed_domains = ["cruzverde.cl"]

  start_urls = ["https://www.cruzverde.cl/medicamentos/"]

  download_delay = 1

  rules = {
    Rule(LinkExtractor(
      allow = r'start=',
      tags = ('a', 'button'),
      attrs = ('href', 'data-url')
    ), follow = True, callback="parse_farmacia")
  }

  def parse_farmacia(self, response):
    sel = Selector(response)
    productos = sel.xpath('//div[@class="col-12 col-lg-4"]')

    for producto in productos:
      item = ItemLoader(Farmacia(), producto)
      item.add_xpath('Nombre', './/div[@class="pdp-link"]/a/text()')
      item.add_xpath('Precio', './/span[@class="value"]/text()')

      yield item.load_item()