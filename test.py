#encoding=utf-8

import os,re,time
import urllib,htmllib

link = urllib.urlopen('http://www.istartedsomething.com/bingimages')
cont = link.readlines()
print cont

for line in cont:
	if re.match('^	<tr><td></td><td></td><td></td><td>',line):
		print line

print time.gmtime()[:3]

#http://cn.bing.com/fd/hpk2/Dover_ROW2439373480.jpg
#http://www.istartedsomething.com/bingimages/resize.php?i=Dover_ROW2439373480.jpg&w=100
#http://www.istartedsomething.com/bingimages/cache/Dover_ROW2439373480.jpg
#^	<tr><td></td><td></td><td></td><td>


