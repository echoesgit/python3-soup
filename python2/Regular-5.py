# encoding:utf-8

import urllib2
import re

url = 'https://search.jd.com/Search?keyword=%E6%8A%80%E6%9C%AF%E4%B9%A6%E7%B1%8D&enc=utf-8&wq=%E6%8A%80%E6%9C%AF%E4%B9%A6%E7%B1%8D&pvid=mo54blzi.4use2o'
req = urllib2.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36","Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4"})
page = urllib2.urlopen(req).read()
p1 = page.find('<div class="fs-cell delivery-location">配送至</div>')

page = page[p1:]

source1 = re.findall(r'<li data-sku="(\d*)" class="gl-item">.*', page)
source2 = re.findall(r'</em><i>(\d+\.\d+)</i>',page)
source3 = re.findall(r'<em>([\x80-\xff]*)</em><i class="promo-words" id="J_AD_\d*',page)
print source3
print len(source1)
print len(source2)
for i in range(len(source1)):
    print source1[i] + '---->' + source2[i]
