from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

from scrapy.crawler import CrawlerProcess

class Noticia(Item):
  titulo = Field()
  descripcion = Field()
  hora = Field()
  img = Field()

class MilenioSpider(Spider):
  name = "SpiderFromMilenio"
  custom_settings = {
    "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
  }
  start_urls = ['https://www.milenio.com/ultima-hora']

  def parse(self, response):
    sel = Selector(response)
    noticias = sel.xpath('//div[@class="list"]/div[@class="lr-row-news"]/div[@class="item-news-container"]')
    for noticia in noticias:
      item = ItemLoader(Noticia(), noticia)
      item.add_xpath('titulo', './div[@class="title-container"]/div[@class="title"]/a/h2/text()')
      item.add_xpath('descripcion', './div[@class="title-container"]/div[@class="summary"]/span/text()')
      item.add_xpath('hora', './div[@class="hour-social-network"]/div/span/text()')
      item.add_xpath('img', './div[@class="img-container"]/a/img/@src')

      yield item.load_item()

#Ejecución
process = CrawlerProcess({
  'FEED_FORMAT': 'json',
  'FEED_URI': 'milenio.json'
})

process.crawl(MilenioSpider)
process.start()