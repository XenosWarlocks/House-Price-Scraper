import scrapy
import json
import csv


class HousespiderSpider(scrapy.Spider):
    name = "houseSpider"
    allowed_domains = [""]
    start_urls = [""]

    def parse(self, response):
        script_content = response.xpath("//script[contains(text(),'window.__PRELOADED_STATE__')]//text()").get()[29:]
        data = json.loads(script_content)
        properties = data['results']['properties']

        for property_item in properties:
            yield{
                'address': property_item['address'],
                'type': property_item['propertyType'],
                'transactions': property_item['transactions'],
                'location': property_item['location'],
                'url': property_item['detailUrl']
            }

        current_page = int(response.url.split('=')[-1])
        if current_page < 40:
            next_page = current_page + 1
            next_url = f"page={next_page}"

            yield response.follow(next_url, callback=self.parse)
