#encoding=utf-8

import os,re
import urllib,httplib,htmllib

link = urllib.urlopen('http://www.zetcode.com')
tmp = link.readlines()
