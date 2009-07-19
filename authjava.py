#encoding=utf-8

import os
import string,re

path = '/ezxlocal/.system/java/DownloadApps/'
filelist = os.listdir('path')
nw1 = 'Domain:Manufacture\n'
#path = '/media/xifs/stools/registry.txt'

def registryit(filename):
	file = open(filename,'r')
	cont = file.readlines()
	file.close()
	for line in cont:
		if re.match('^Domain',line):
			fina = line
	idx = cont.index(fina)
	cont.pop(idx)
	cont.insert(idx,nw1)
	file = open(path,'w')
	file.writelines(cont)
	file.close()
	
if __name__ == '__main__':
	for filedir in filelist:
		filename = path + filedir + 'registry.txt'
		registryit(filename)
	print 'success'