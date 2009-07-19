#encoding=utf-8

import time

def lifetime(x,y,z):
	u,v,w = time.gmtime()[0:3]
	timenow = time.mktime((u,v,w,0,0,0,0,0,0))
	timebir = time.mktime((x,y,z,0,0,0,0,0,0))
	(year,month,day) = time.gmtime(timenow-timebir)[0:3]
	year -= 1970
	month -= 1
	day -= 1
	return year,month,day
	
def oldtime():
	lt = ['子','丑','丑','寅','寅','卯','卯','辰','辰','巳','巳','午','午','未','未','申','申','酉','酉','戌','戌','亥','亥','子']
	return lt[time.localtime()[3]]

def gengtime():
	if oldtime() == '戌' :
		return '一更'
	elif oldtime() == '亥' :
		return '二更'
	elif oldtime() == '子' :
		return '三更'
	elif oldtime() == '丑' :
		return '四更'
	elif oldtime() == '寅' :
		return '五更'
	else:
		return '没到晚上'		

if __name__ == '__main__':
	print 'today is ',time.gmtime()[0:3]
	print 'your lifetime is ',lifetime(1987,9,27)
	print 'now is ',time.localtime()[3:6]
	print oldtime()
	print gengtime()