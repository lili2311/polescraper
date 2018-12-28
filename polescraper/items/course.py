import scrapy


class CourseItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()

