#encoding=utf-8

import string,base64

link = 'QUFodHRwOi8vNjAuMTkxLjYwLjEwODo4MDgwL3hweGlhemFpL0RlZXBpbl9HaG9zdF9YUF9WMTguMC5pc29aWg=='

print base64.decodestring(link)[2:-2]

print base64.decodestring('aW14aWZzQGdtYWlsLmNvbQ==')

print base64.decodestring('ZmVpaHUucm9nZXJAZ21haWwuY29t')

#http://www.google.com/latitude/apps/badge/api?user=-303550281279573224&type=json



import urllib
import re
f = urllib.urlopen("http://www.google.com/")
raw_html = f.read()
patt = """<title>([^<]*)</title>"""
all = re.findall(patt, raw_html, re.IGNORECASE)
title = "".join(all)
print title