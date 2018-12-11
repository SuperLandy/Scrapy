
一、 安装scrapy-splash

        在docker中安装scrapy-splash
        启动docker后执行

docker run -p 8050:8050 scrapinghub/splash

二、 修改spiders设置
    2.1 爬虫主文件代码



# -*- coding: utf-8 -*-
import scrapy
from  scrapy_splash import SplashRequest,SplashFormRequest   #导入SplashRequest
from  dytt.items import DyttItem                             #导入item
class DyttSpider(scrapy.Spider): 
    name = 'dyttspider'
    def start_requests(self):
        splash_args = {"lua_source": """                     #设置splash_args
                            --splash.response_body_enabled = true
                            splash.private_mode_enabled = false
                            assert(splash:go("https://item.jd.com/5089253.html"))       #需要js渲染的网页
                            splash:wait(3)
                            return {html = splash:html()}
                            """}
        yield SplashRequest('https://item.jd.com/5089253.html',args=splash_args,endpoint='run',callback=self.parse)


    def parse(self, response):             #回调函数，分析结果
        item = DyttItem()
        info = response.xpath('//div[@class="sku-name"]/text()').extract()
        for title in info:
            item['title'] = titile.strip('\n').strip(' ')                       #返回商品名
        item['dt'] =  response.xpath('//span[@class="price J-p-5089253"]/text()').extract() #商品价格
        yield item
        
  


  2.2  修改 settings.py文件
        


# -*- coding: utf-8 -*-

BOT_NAME = 'dytt'

SPIDER_MODULES = ['dytt.spiders']
NEWSPIDER_MODULE = 'dytt.spiders'


#设置代理
USER_AGENT = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",

]

#遵循rebotstxt协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

#下载时间间隔
DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

#开启cache
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# 设置请求头
DEFAULT_REQUEST_HEADERS = {
    'Referer': 'https://www.dytt8.net/',
    "Content-Type": "text/plain;charset=UTF-8",
}


#开启scrapy_splash中间件
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

#设置scrapy-splash地址，启用相应中间件
SPLASH_URL = "http://192.168.91.40:8050/"
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,  # 不配置查不到信息
    #'dytt.middlewares.DyttDownloaderMiddleware': 543,
}


#开启httpcache
HTTPCACHE_ENABLED = True

#缓存目录
HTTPCACHE_DIR = 'httpcache'

#
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
HTTPERROR_ALLOWED_CODES = [400,403]


三、保存文件乱码，解决办法
-s FEED_EXPORT_ENCODING=utf-8
