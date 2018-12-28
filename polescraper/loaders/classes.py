import dateparser
from scrapy.loader import ItemLoader
from polescraper.items.classes import ClassItem
from scrapy.loader.processors import MapCompose, TakeFirst, Join

def parse_date(date):
  return dateparser.parse(date)

class ClassLoader(ItemLoader):
  default_item_class = ClassItem
  end_time_out = TakeFirst()
  start_time_out = TakeFirst()
  title_out = TakeFirst()
  url_out = TakeFirst()

