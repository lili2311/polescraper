# -*- coding: utf-8 -*-
import scrapy
import json
from urllib.parse import urlencode
import datetime
from dateutil import relativedelta
from polescraper.loaders.classes import ClassLoader
from polescraper.items.classes import ClassItem


class PolePeopleClassesSpider(scrapy.Spider):
    name = "polepeople_classes"

    def start_requests(self):
        thisdate = datetime.date.today()
        nextdate = datetime.date.today() + relativedelta.relativedelta(months=1)
        this_key = f'{thisdate.year}-{thisdate.month}'
        next_key = f'{nextdate.year}-{nextdate.month}'
        params = {
            'feed_type': 'provider',
            'feed_type_id': '891621',
            'keys': f'{this_key},{next_key}'

        }
        url = 'https://goteamup.com/event_feed/?' + urlencode(params)

        yield scrapy.Request(url=url, callback=self.parse_class_list)

    def parse_class_list(self, response):
        classes_data = json.loads(response.body_as_unicode())
        for data in classes_data['events']:
            import pprint
            pprint.pprint(data)
            loader = ClassLoader(selector=data)
            url = data.get('registration_url');
            if (url):
                loader.add_value('url', 'https://www.goteamup.com' + url)
            loader.add_value('title', data['name'])
            loader.add_value('start_time', data['start'])
            loader.add_value('end_time', data['end'])

            yield loader.load_item()


