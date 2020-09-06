# Scrapy settings for wangpin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wangpin'

SPIDER_MODULES = ['wangpin.spiders']
NEWSPIDER_MODULE = 'wangpin.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'wangpin (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
    'Cookie': "bid=hbqXLC6YCvU; __utmc=30149280; __utmz=30149280.1598191196.1.1.utmcsr=(direct)"
              "|utmccn=(direct)|utmcmd=(none); __utmc=223695111; __utmz=223695111.1598191196.1.1.utmcsr=(direct)"
              "|utmccn=(direct)|utmcmd=(none); ll='118282'; __yadk_uid=s6KCUNejCZhM44JxTsNzQIxEK0YXdZ2V;"
              " _vwo_uuid_v2=D5977CEBED71C53D8107AA6515834D00B|eaae6b8c887070d65f25c419cecd22b0; _pk_ses.100001.4cf6=*;"
              " ap_v=0,6.0; __utma=30149280.2091494749.1598191196.1598195848.1598277246.3; __"
              "utmb=30149280.0.10.1598277246; __utma=223695111.677151737.1598191196.1598195848.1598277246.3; __"
              "utmb=223695111.0.10.1598277246; _pk_id.100001.4cf6=f3d2ba0518799a9a.1598191196.3.1598277953.1598195848."
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'wangpin.middlewares.WangpinSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wangpin.middlewares.WangpinDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'wangpin.pipelines.WangpinPipeline': 300,
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
