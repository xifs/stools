#encoding=utf-8

from sgmllib import SGMLParser
import urllib

class URLLister(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.urls = []

	def start_a(self, attrs):
		href = [v for k, v in attrs if k=='href']
		if href:
			self.urls.extend(href)


usock = urllib.urlopen("http://repo.archlinux.fr/i686")
parser = URLLister()
parser.feed(usock.read())
usock.close()
parser.close()
for url in parser.urls: print url
