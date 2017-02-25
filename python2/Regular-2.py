# encoding = utf-8

import urllib2
import re


def mena_audience_score(FilmId):
    arv = 0
    count = 0
    u = 'http://movie.mtime.com/'+`FilmId`
    req = urllib2.Request(u, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"})
    pagedata = urllib2.urlopen(req).read()
    source = re.findall(r'<span class="db_point ml6">(.*)</span>',pagedata)
    for s in source:
        count = count+1
        arv += float(s)

    return arv/count
print mena_audience_score(194595)
