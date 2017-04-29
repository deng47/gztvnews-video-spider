'''
tags=soup.select('a')

for tag in tags:
    if len(dic)+1 > limit:
        break
    link = tag.get('href')[4:-2]
    if link.startswith('www.bilibili') and re.search(r'[^\x00-\xff]',tag.text)!=None:
        link=link[:link.find('?from')]
        dic[tag.text[10:-8]+' http://'+link] = []
'''


import requests
import json
import urllib
import re
from bs4 import BeautifulSoup


url='http://news.gztv.com/guangshi/'
req=urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36')
response=urllib.request.urlopen(req)
html=response.read().decode('utf8')
soup=BeautifulSoup(html, "html.parser")

tags=soup.select('img')
for tag in tags:
    link=tag.get('src')
    if re.search('rtmp', link)!=None:
        print(link[:-7]+'1.mp4')
