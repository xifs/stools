#encoding=utf-8

import os
import string,re,time
'''
filename = '/proc/net/dev'

file = open(filename,'r')
cont = file.readlines()
file.close()
for line in cont:
	if re.match('^ wlan0',line):
		fina = line

src = string.split(fina,'   ')
rx , tx = src[0].split(' ')[1][6:] , src[10].split(' ')[1]
prx , ptx = src[0].split(' ')[3] , src[10].split(' ')[3]

print "RX:",(rx)," , PRX:",(prx)
print "TX:",(tx)," , PTX:",(ptx)
'''


def netspeed():
	r = re.compile( r"^\s*" + re.escape('wlan0') + r":(.*)$", re.MULTILINE )
	f = open('/proc/net/dev')
	dev_lines = f.read()
	f.close()
	match = r.search(dev_lines)
	parts = match.group(1).split()
	return long(parts[0]),long(parts[8])
a,b = netspeed()
time.sleep(1)
c,d = netspeed()

print c-a,d-b