#encoding=utf-8

import os,re
import urllib,httplib,htmllib

#link = httplib.HTTPConnection('www.zetcode.com')
#link.request('GET','/index.html')
#tmp = link.getresponse().read()

link = urllib.urlopen('http://www.zetcode.com')
tmp = link.readlines()

for line in tmp:
	if re.match('^<div style=";color:#343434; margin-left:1%;font-size:11px">Last updated',line):
		res = line

print res[72:-84]

import urllib
import re
f = urllib.urlopen("http://www.zetcode.com")
raw_html = f.read()
patt = """<title>([^<]*)</title>"""
all = re.findall(patt, raw_html, re.IGNORECASE)
title = "".join(all)
print title

last = 'June 28, 2009'
