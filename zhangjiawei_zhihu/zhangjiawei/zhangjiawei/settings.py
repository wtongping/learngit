# -*- coding: utf-8 -*-

# Scrapy settings for zhangjiawei project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhangjiawei'

SPIDER_MODULES = ['zhangjiawei.spiders']
NEWSPIDER_MODULE = 'zhangjiawei.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhangjiawei (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIE = {'aliyungf_tc': 'AQAAAIvRHSrgvwMAFMhHfSHt87GcbOwF', 'r_cap_id': 'NzlhMzE2Zjc3Y2Q4NGIyOWJkZDc5ZjExOGVkZjYyNTU', '__utma': '51854390.1463051529.1508762389.1508762389.1508762389.1', 'cap_id': 'Njg4MzlmNWUwZDczNGZkNWJmYjM5ZGYxM2ExZjEzMjc', '_xsrf': '35b564a9-40bc-4f85-b93a-92de25a457d4', 'd_c0': 'AAACa5H_fwyPTtvuNrHg2WD6U4GbEaOHB3A', '__utmz': '51854390.1508762389.1.1.utmcsr', 'z_c0': 'Mi4xcURZbUFBQUFBQUFBQUFKcmtmOV9EQmNBQUFCaEFsVk51Q1BiV2dEOUpRX3RJS3BTV3FJYnVQWmZBcUIzMlh6aWtR|1508758968|479c2df6d37351ce5ca0edd1bda29c58cabc7c55', '__utmv': '51854390.100-1|2', 'q_c1': '016793dc7a344cb0acedfc1abd01ee3f|1507526725000|1507526725000', '_zap': 'f4759d15-d3bc-4002-88a2-b18ef1e16d66'}
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhangjiawei.middlewares.ZhangjiaweiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhangjiawei.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhangjiawei.pipelines.ZhangjiaweiPipeline': 100,
}
#ITEM_PIPELINES = {
#    'zhangjiawei.pipelines.Url_token_Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
