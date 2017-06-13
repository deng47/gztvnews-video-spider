'''
This program crawls news.gztv.com and searches for streaming video addresses
Input: no input
Output: urls of news videos
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
