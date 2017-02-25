# encoding:utf-8

import urllib2
import re

url = 'http://58921.com/'
req = urllib2.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"})
pagedata = urllib2.urlopen(req).read()

s1 = pagedata.find("<th>电影名称</th><th>总场次/占比</th><th>网票票房</th>")
s2 = pagedata[s1:].find('<span class="form_description">各平台场次存在重叠，实时与预计票房为程序自行计算，仅供参考</span>')

data = pagedata[s1:s1+s2]

print data
source = re.findall(r'<tr class="[a-z]{3,4}"><td><a href="/film/[\d]+/boxoffice".+', data)
ss = 0
for s in source:
    lin = re.findall(r'(\d+[\.]?\d+[%]?[\u4e00-\u9fa5]?)',s)
    print lin
    print lin[-3]
    ss = ss+ float(lin[-3])

print ss
