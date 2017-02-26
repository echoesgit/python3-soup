# encoding:utf-8
'''
regular web page in url
'''
import urllib2
import re


def mena_audience_score(FilmId):
    arv = 0
    count = 0
    u = 'http://movie.mtime.com/'+FilmId
    req = urllib2.Request(u, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"})
    pagedata = urllib2.urlopen(req).read()
    source = re.findall(r'<span class="db_point ml6">(.*)</span>',pagedata)
    for s in source:
        count = count+1
        arv += float(s)

    if count != 0:
        return arv/count
    return 0



url = 'http://theater.mtime.com/China_Beijing/'
req = urllib2.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"})

pagedata = urllib2.urlopen(req).read()
urls = re.findall(r'<a href="http://movie.mtime.com/(.*)/" target="_blank" title="(.*)\" class',pagedata)
for u in urls:

    print u[0]+'--'+u[1].decode('utf-8') + '------>'
    print mena_audience_score(u[0])



