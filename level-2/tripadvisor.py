from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Opinion(Item):
  # titulo = Field()
  # calificacion = Field()
  contenido = Field()
  autor = Field()

class TripAdvidor(CrawlSpider):
  name = "OpinionesTripAdvisor"
  custom_settings = {
    "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    'CLOSESPIDER_PAGECOUNT': 20
  }

  allowed_domains = ['tripadvisor.com']
  start_urls = ['https://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html']

  download_delay = 1

  rules = (
    #Horizontalidad de hoteles h
    Rule(
      LinkExtractor(
        allow = r'-oa\d+-'
      ), follow = True
    ),
    #Detalle de hoteles v
    Rule(
      LinkExtractor(
        allow = r'/Hotel_Review-',
        restrict_xpaths=['//div[@id="taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0"]//a[@data-clicksource="HotelName"]']
      ), follow = True
    ),
    #Paginacion de opiniones dentro de un Hotel h
    Rule(
      LinkExtractor(
        allow = r'-or\d+-'
      ), follow = True
    ),
    #Detalle de perfil de usuario v
    Rule(
      LinkExtractor(
        allow = r'/Profile/',
        restrict_xpaths=['//div[@data-test-target="reviews-tab"]//a[contains(@class, "ui_header")]']
      ), follow = True, callback="parse_opinion"
    )
  )

  def parse_opinion(self, response):
    sel = Selector(response)
    opiniones = sel.xpath('//div[@id="content"]/div/div')
    autor = sel.xpath('//h1/span/text()').get()

    for opinion in opiniones:
      item = ItemLoader(Opinion(), opinion)
      item.add_value('autor', autor)
      # item.add_xpath('titulo', '//div[@class="]')
      item.add_xpath('contenido', './/q/text()')
      # item.add_xpath('calificacion', '')

      yield item.load_item()