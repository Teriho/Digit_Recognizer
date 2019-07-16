#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:18:15 2018

@author: eric
"""
from urllib import request 
import re

#data = request.urlopen("http://dl.pconline.com.cn/sort/87.html").read()
data = request.urlopen("http://dl.pconline.com.cn/sort/2288.html").read()

data = str(data,encoding = "gb2312")
#print(data)

pat1 = "<!-- wraper -->([\s\S]*)<!-- sc-1 -->"
pat2 = "<div class=\"crumb\">([\s\S]*?)</div>"
pat3 = "title=(.*?)>(.*?)</a>"


pat4 = "<div class=\"list-item-left\">([\s\S]*?)<p class=\"art-info\">"
pat5 = "<p class=\"title\">([\s\S]*?)<div class=\"pic-txt\">"
pat6 = "title=\"(.*?)\">"
pat7 = "<p class=\"des\">(.*?)</p>"


result1 = re.compile(pat1).findall(data)
result2 = re.compile(pat2).findall(result1[0])
result3 = re.compile(pat3).findall(result2[0])


result4 = re.compile(pat4).findall(data)
result5 = re.compile(pat5).findall(result4[0])
result6 = re.compile(pat6).findall(result5[0])
result7 = re.compile(pat7).findall(result4[0])
#result = re.match(pat,data)

print('\n'+result6[0]+'\n')
print(result7[0])



#type(data)