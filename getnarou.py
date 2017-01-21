#!/usr/bin/env python
#coding: utf-8

import requests as rq
from bs4 import BeautifulSoup as sp
from urllib.parse import urljoin
import re

def flatlist(lis):
	#This list is mountain [[[],[]],[[],[]],[[],[]]] -> [,,,,,,,,]
	#return [e for inlis in lis for e in inlis]
	flatlist=[]
	for e in lis:
		flatlist.extend(e)
	return flatlist





wanturl="http://web.archive.org/web/20131127132412/http://ncode.syosetu.com/n7145bl"

htmin=rq.get(wanturl)
htmin.encoding="utf-8"
naiyou=sp(htmin.text,"lxml")

tdtab = naiyou.find_all('td',class_="period_subtitle")
atab=[a.find_all("a") for a in tdtab]

atab=flatlist(atab)

link=[a.get("href") for a in atab]

url="http://web.archive.org"
sinurl=[urljoin(url,path) for path in link]


onon=rq.get(sinurl[0])
one=sp(onon.text,"lxml")




print(one)
