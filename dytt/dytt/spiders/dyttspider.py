# -*- coding: utf-8 -*-
import scrapy
from  scrapy_splash import SplashRequest,SplashFormRequest
from  dytt.items import DyttItem
class DyttSpider(scrapy.Spider):
    name = 'dyttspider'
    def start_requests(self):
        splash_args = {"lua_source": """
                            --splash.response_body_enabled = true
                            splash.private_mode_enabled = false 
                            assert(splash:go("https://item.jd.com/5089253.html"))
                            splash:wait(3)
                            return {html = splash:html()}
                            """}
        yield SplashRequest('https://item.jd.com/5089253.html',args=splash_args,endpoint='run',callback=self.parse)


    def parse(self, response):
        item = DyttItem()
        inf = response.xpath('//div[@class="sku-name"]/text()').extract()
        for an in inf:
            item['title'] = an.strip('\n').strip(' ')
        item['dt'] =  response.xpath('//span[@class="price J-p-5089253"]/text()').extract()
        yield item
