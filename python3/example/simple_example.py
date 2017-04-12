# -*- coding: utf-8 -*-
from urllib import request
from http import cookiejar
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
#req = request.Request(url=" http://blog.csdn.net/" , headers=headers)
#content = request.urlopen(req).read().decode("utf-8")
#print(content)

cookies_support = request.HTTPCookieProcessor(cookiejar.CookieJar())
opener = request.build_opener(cookies_support , request.HTTPHandler)
request.install_opener(opener)

content = request.urlopen(url="http://www.baidu.com" ).read()
print(content)
