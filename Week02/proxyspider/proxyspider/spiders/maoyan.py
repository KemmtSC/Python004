import scrapy
from scrapy.selector import Selector
from proxyspider.items import ProxyspiderItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = 'http://maoyan.com/films?showType=3'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        movies_info = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for i,movie in enumerate(movies_info):
            if i > 9:
                break

            item = ProxyspiderItem()
            item['movie_name'] = movie.xpath('./div/span/text()').get()
            item['movie_score'] = movie.xpath('./div/span[@class="score channel-detail-orange"]').xpath('string(.)').get(default='暂无')
            item['movie_type'] = str(movie.xpath('./div[1]/following-sibling::div[1]/text()').getall()[1]).strip()
            item['movie_actor'] = str(movie.xpath('./div[1]/following-sibling::div[2]/text()').getall()[1]).strip()
            item['movie_time'] = str(movie.xpath('./div[1]/following-sibling::div[3]/text()').getall()[1]).strip()
                
            yield item
