import scrapy, six
from full.items import FullItem

class DmozSpider(scrapy.Spider):
    name = "full"
    allowed_domains = ["win4000.com"]
    start_urls = [
        "http://www.win4000.com/wallpaper_detail_153260.html",
        "http://www.win4000.com/wallpaper_detail_153260_2.html",
        "http://www.win4000.com/wallpaper_detail_153260_3.html",
        "http://www.win4000.com/wallpaper_detail_153260_4.html",
        "http://www.win4000.com/wallpaper_detail_153260_5.html",
        "http://www.win4000.com/wallpaper_detail_153260_6.html",
        "http://www.win4000.com/wallpaper_detail_153260_7.html",
        "http://www.win4000.com/wallpaper_detail_153260_8.html",
        "http://www.win4000.com/wallpaper_detail_153260_9.html",
    ]

    def parse(self, response):# 必须是可迭代对象，否则报错
        #获取图片链接地址
        src_link = response.xpath('//div/a/img[@class="pic-large"][@src]/@src').extract()

        # 获取图片链接地址
        src_link = response.xpath('//div/a/img[@class="pic-large"][@src]/@src').extract()

        # 初始化item赋值给item的中image_urls并返回可迭代对象
        item = FullItem()
        item['image_urls'] = src_link
        yield item

        #也可使用如下办法
        # for link  in six.moves.zip(src_link):
        #     item = FullItem()
        #     item['image_urls']= link
        #     yield item

