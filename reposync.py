#encoding=utf-8
import os,sys,re
from ftplib import FTP

remoterepo='ftp.archlinux.org'

remote=FTP(remoterepo)
remote.login()
print('Login Succeeded')
print('Get db file')
remote.retrbinary('RETR '+'/core/os/i686/core.files.tar.gz',open('/tmp/core.files.tar.gz','wb').write)

os.chdir('/tmp')
newlst = os.popen('bsdtar -tf /tmp/core.files.tar.gz').readlines()

print newlst
#for line in newlst:
#if re.match('depends',line):
x = 0
l = [0]
a = 0
while a<100:
	x = x + 3
	l.append(x)
	a = a + 1
lst = []
for n in l:
	lst.append(newlst[n])


