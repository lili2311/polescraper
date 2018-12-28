# -*- coding: utf-8 -*-
import scrapy
from polescraper.loaders.course import CourseLoader
from polescraper.items.course import CourseItem


class PolePeopleSpider(scrapy.Spider):
    name = "polepeople"

    def start_requests(self):
        url = 'https://goteamup.com/p/891621-polepeople-dance-fitness/courses/'

        yield scrapy.Request(url=url, callback=self.parse_course_list)

    def parse_course_list(self, response):
        courses_data = response.css('.well-list .well-row')
        for course_selector in courses_data:
          loader = CourseLoader(selector=course_selector)
          loader.add_css('title', '.primary-text::text')
          date = course_selector.css('.more-details li:first-of-type::text').extract()[0]
          start_date, end_date = date.split('–')
          loader.add_value('start_date', start_date)
          loader.add_value('end_date', end_date)
          yield loader.load_item()


