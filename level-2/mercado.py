from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

# from scrapy.crawler import CrawlerProcess

class Articulo(Item):
  titulo = Field()
  precio = Field()
  descripcion = Field()

class MercadoLibreCrawler(CrawlSpider):
  name = 'mercadoLibre'
  custom_settings = {
    "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    'CLOSESPIDER_PAGECOUNT': 2
  }

  download_delay = 1

  allowed_domains = ['listado.mercadolibre.com.mx', 'articulo.mercadolibre.com.mx']

  start_urls = ['https://listado.mercadolibre.com.mx/webcam']

  rules = (
    # paginacion, no visita identicas
    Rule(
      LinkExtractor(
        allow = r'/_Desde_'
      ), follow = True, 
    ),
    # Detalle de los productos
    Rule(
      LinkExtractor(
        allow = r'/MLM-'
      ), follow = True, callback='parse_items'
    )
  )

  def limpiarTexto(self, texto):
    nuevoTexto = texto.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
    return nuevoTexto

  def parse_items(self, response): 
    item = ItemLoader(Articulo(), response)
    item.add_xpath('titulo', '//h1/text()', MapCompose(self.limpiarTexto))
    item.add_xpath('descripcion', '//p[@class="ui-pdp-description__content"]/text()', MapCompose(self.limpiarTexto))
    item.add_xpath('precio', '//div[@class="ui-pdp-price__second-line"]//span[@class="price-tag-fraction"]/text()')

    yield item.load_item()


# #Ejecución
# process = CrawlerProcess({
#   'FEED_FORMAT': 'json',
#   'FEED_URI': 'mercado.json'
# })

# process.crawl(MercadoLibreCrawler)
# process.start()
