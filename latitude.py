#encoding=utf-8

import os
import urllib,json

url = 'http://www.google.com/latitude/apps/badge/api?user=-303550281279573224&type=json'
s = json.loads(urllib.urlopen(url).read())

print s
reverseGeocode = json.loads(s)
#print str(len(reverseGeocode))
#print reverseGeocode

#m = hashlib.md5().update(src)
#dest= m.hexdigest()   