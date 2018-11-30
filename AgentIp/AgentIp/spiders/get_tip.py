import scrapy, six
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from urllib import request


class DmozSpider(scrapy.Spider):
    name = "getip"
    allowed_domains = ["kuaidaili.com"]
    start_urls = [
        "https://www.kuaidaili.com/free/inha/"

    ]

    def parse(self, response):
        respon_ip = response.xpath('//tr//td[@data-title="IP"]/text()').extract()
        respon_port = response.xpath('//tr//td[@data-title="PORT"]/text()').extract()
        for ip, port in six.moves.zip(respon_ip, respon_port):
            ip_addr = ('%s' + ':' + '%s') % (ip, port)
            print('发现代理IP：' + ip_addr)
            with open('D:\mypython\\agent_ip.txt', 'a+', encoding='utf-8') as f:
                f.write(ip_addr + '\n')
        f.close()
