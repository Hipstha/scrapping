from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy import Request

class Dummy(Item):
  titulo = Field() # Titulo de pagina que embebe al iframe
  titulo_iframe = Field() # Titulo de pagina del iframe

class W3SCrawler(Spider):
  name = 'w3s'
  custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
    'REDIRECT_ENABLED': True # Parametro para activar los redirects (codigo 302)
  }

  allowed_domains = ['w3schools.com']
  start_urls = ['https://www.w3schools.com/html/html_iframe.asp']

  download_delay = 1

  def parse(self, response):
    sel = Selector(response)
    titulo = sel.xpath('//div[@id="main"]//h1/span/text()').get()
    
    previous_data = {
      'titulo': titulo
    }
    
    iframe_url = sel.xpath('//div[@id="main"]//iframe[@width="99%"]/@src').get()

    iframe_url = "https://www.w3schools.com/html/" + iframe_url

    yield Request(iframe_url, callback=self.parse_iframe, meta=previous_data)

  def parse_iframe(self, response):
    item = ItemLoader(Dummy(), response)
    item.add_xpath('titulo_iframe', '//div[@id="main"]//h1/span/text()')
    item.add_value('titulo', response.meta.get('titulo'))

    print(response.meta.get('titulo'))
    yield item.load_item()