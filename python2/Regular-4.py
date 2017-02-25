# encoding:utf-8
'''
一定要注意正则匹配汉字[\x80-\xff]
'''
import urllib2
import re

url = 'http://www.quanji.la/'
req = urllib2.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"})
pagedata = urllib2.urlopen(req).read()
s1 = pagedata.find('<h2>最新电影</h2>')
s2 = pagedata[s1:].find('<h2>最新电视剧</h2>')
data = pagedata[s1:s1+s2]
source = re.findall(r'<li><p>[<]?[e]?[m]?[>]?([\d]{2}-[\d]{2})[<]?[/]?[e]?[m]?[>]?</p>([\x80-\xff]*)<a href="http://www.quanji.la/Juqingdianying/[A-Z]+[0-9]+/">([\x80-\xff]*)</a></li>', data)

for it in source:
    print it[0] + '---' +it[1]+'---'+it[2]