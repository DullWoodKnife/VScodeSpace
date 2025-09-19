# scrapy

## 认识scrapy

scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架，我们只需实现少量的代码，就能实现数据的快速抓取

> **scrapy使用了Twisted异步网络架构，可以加快下载速度  pip install twisted**

安装：pip install scrapy 



## 流程图

![](.\image\scrapy流程.png)



### 组件介绍

| 组件                             | 作用                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| Scrapy Engine(引擎)              | 负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等 |
| Scheduler(调度器)                | 它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎 |
| Downloader(下载器)               | 负责下载(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理。 |
| Spider(爬虫)                     | 它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler |
| Item Pipeline(管道)              | 它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方 |
| Downloader Middlewares下载中间件 | 一个可以自定义扩展下载功能的组件。                           |
| Spider Middlewares(Spider中间件) | 一个可以自定扩展和操作引擎和Spider中间通信的功能组件         |



### 运行流程



-  引擎：Hi！Spider, 你要处理哪一个网站？
-  Spider：老大要我处理xxxx.com。
-  引擎：你把第一个需要处理的URL给我吧。
-  Spider：给你，第一个URL是xxxxxxx.com。
-  引擎：Hi！调度器，我这有request请求你帮我排序入队一下。
-  调度器：好的，正在处理你等一下。
-  引擎：Hi！调度器，把你处理好的request请求给我。
-  调度器：给你，这是我处理好的request
-  引擎：Hi！下载器，你按照老大的下载中间件的设置帮我下载一下这个request请求
-  下载器：好的！给你，这是下载好的东西。（如果失败：sorry，这个request下载失败了。然后引擎告诉调度器，这个request下载失败了，你记录一下，我们待会儿再下载）
-  引擎：Hi！Spider，这是下载好的东西，并且已经按照老大的下载中间件处理过了，你自己处理一下（注意！这儿responses默认是交给**def parse()**这个函数处理的）
-  Spider：（处理完毕数据之后对于需要跟进的URL），Hi！引擎，我这里有两个结果，这个是我需要跟进的URL，还有这个是我获取到的Item数据。
-  引擎：Hi ！管道 我这儿有个item你帮我处理一下！调度器！这是需要跟进URL你帮我处理下。然后从第四步开始循环，直到获取完老大需要全部信息。
-  管道调度器：好的，现在就做！

------



## 快速入门

* 创建一个scrapy项目

~~~python
scrapy startproject name	# name 为项目名称
~~~

* 创建一个spider

~~~python
cd name		# 进入创建的项目

scrapy genspider spider_name url  # spider_name为爬虫名，url为要抓取的目标网站

scrapy crawl spider_name   # 执行爬虫
~~~

------



### spider

手动创建的spider文件

~~~python
import scrapy


class BdSpiderSpider(scrapy.Spider):
    name = 'spider_name'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com']

    def parse(self, response,**kwargs):
        pass
~~~

* **name：**标识spider。它在一个项目中必须是唯一的，即不能为不同的爬行器设置相同的名称

* **allowed_domains：**允许爬取url的域名

* **start_urls：**一个url列表，spider从这些网页开始抓取

* **parse():**一个方法，当start_urls里面的网页抓取下来之后需要调用这个方法解析网页内容

------



### items

定义抓取的字段名

~~~python
import scrapy


class MySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
~~~

------



### pipeline

数据存储的位置

~~~pass
from itemadapter import ItemAdapter


class MySpiderPipeline:
    def process_item(self, item, spider):
        return item

~~~



### settings

项目配置文件

~~~python
# Scrapy settings for my_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'my_spider'

SPIDER_MODULES = ['my_spider.spiders']
NEWSPIDER_MODULE = 'my_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'

# Obey robots.txt rules
# robots协议，默认遵守
ROBOTSTXT_OBEY = False
# 日志等级，ERROR最高
LOG_LEVEL = "ERROR"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 并发请求(concurrent requests)的最大值
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# 下载延迟
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 对单个网站进行并发请求的最大值
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 对单个IP进行并发请求的最大值。如果非0，则忽略
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'my_spider.middlewares.MySpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'my_spider.middlewares.MySpiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
     # 优先级  数字越小，越靠近管道
    'my_spider.pipelines.MySpiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

~~~



