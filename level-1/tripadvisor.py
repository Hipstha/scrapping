from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Hotel(Item):
  nombre = Field()
  precio = Field()
  descripcion = Field()
  amenities = Field()

class TripAdvisor(CrawlSpider):
  name = "Hoteles"
  custom_settings = {
    "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
  }
  start_urls = ['https://www.tripadvisor.com.mx/Hotels-g150782-Monterrey_Northern_Mexico-Hotels.html']

  #tiempo que espera scrapy para nuevo requerimiento
  download_delay = 2

  rules = (
    Rule(
      LinkExtractor(
        allow = r'/Hotel_Review-'
      ), follow = True, callback="parse_hotel"
    )
  )

  def quitarSimboloDolar(self, texto):
    nuevoTexto = texto.replace("$", "")
    nuevoTexto = nuevoTexto.replace('\n', '').replace('\r', '').replace('\t', '')
    return nuevoTexto

  def parse_hotel(self, response):
    sel = Selector(response)
    item = ItemLoader(Hotel(), sel)

    item.add_xpath('nombre', '//h1[@id="HEADING"]/text()')
    item.add_xpath('precio', '//div[@class="hotels-hotel.offers.DominantOffer__price--D-ycN"]/text()', MapCompose(self.quitarSimboloDolar))
    item.add_xpath('descripcion', '//div[contains(@class, "hotel-review-about-csr-Description__description")]/div[1]/text')
    item.add_xpath('amenities', '//div[contains(@class, "hotels-hr-about-amenities-Amenity__amenity")]/text()')

    yield item.load_item()