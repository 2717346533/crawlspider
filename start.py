#开发人员：林泽鑫
#开发实践：2019/7/30 23:59
#文件名称：start.py.py
#开发工具: PyCharm
from scrapy import cmdline

cmdline.execute("scrapy crawl wxapp_spider".split())