import dateparser
from scrapy.loader import ItemLoader
from polescraper.items.course import CourseItem
from scrapy.loader.processors import MapCompose, TakeFirst, Join

def parse_date(date):
  return dateparser.parse(date)

class CourseLoader(ItemLoader):
  default_item_class = CourseItem
  title_in = MapCompose(str.strip)
  title_out = Join()
  start_date_in = MapCompose(str.strip, parse_date)
  start_date_out = TakeFirst()
  end_date_in = MapCompose(str.strip, parse_date)
  end_date_out = TakeFirst()
