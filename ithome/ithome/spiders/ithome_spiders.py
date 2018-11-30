import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from urllib import request


class DmozSpider(scrapy.Spider):
    name = "it"
    allowed_domains = ["mi25.cn"]
    start_urls = [
        "http://mi25.cn/req/page/user/User/login"
        # "http://www.nipic.com/show/21527552.html"
    ]

    def parse(self, response):
        print(response.request.headers["User-Agent"])

        # link = response.xpath('//div[@id="static"]/img[contains(@src,"http://")]/@src').extract()
        # title = response.xpath('//div[@id="static"]/img[contains(@src,"http://")]/@alt').extract()
        # print(title,'\n',link)
        # filename = title[0] + '.jpg'
        # # url = link[0]
        # print(filename)
        # request.urlretrieve(filename=filename,url=url)
