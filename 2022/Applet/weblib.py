from msilib.schema import Property
import webbrowser
import requests
baidu = "baidu.com/s?wd="
bing = "bing.com/search?q="
google = "google.com/search?q="
STATUS = {
100:"Continue",
101:"Switching Protocols",
200:"OK",
201:"Created",
202:"Accepted",
203:"Non-Authoritative Information",
204:"No Content",
205:"Reset Content",
206:"Partial Content",
300:"Multiple Choices",
301:"Moved Permanently",
302:"Found",
303:"See Other",
304:"Not Modified",
305:"Use Proxy",
306:"Unused",
307:"Temporary Redirect",
400:"Bad Request",
401:"Unauthorized",
402:"Payment Required",
403:"Forbidden",
404:"Not Found",
405:"Method Not Allowed",
406:"Not Acceptable",
407:"Proxy Authentication Required",
408:"Request Time-out",
409:"Conflict",
410:"Gone",
411:"Length Required",
412:"Precondition Failed",
413:"Request Entity Too Large",
414:"Request-URI Too Large",
415:"Unsupported Media Type",
416:"Requested range not satisfiable",
417:"Expectation Failed",
500:"Internal Server Error",
501:"Not Implemented",
502:"Bad Gateway",
503:"Service Unavailable",
504:"Gateway Time-out",
505:"HTTP Version not supported",
}


class Client(object):
	def __init__(self,site = "about:blank"):
		self.site = site
	@property
	def open(self):
		webbrowser.open(self.site)
	def search(self,kw):
		webbrowser.open(self.site+kw)
	def setsite(self,name):
		self.site = name
	@property
	def clear(self):
		self.site = "about:blank"
		return 0

class Request(object):
    def __init__(self,site = "about:blank"):
        self.connect = requests.get(site)
		self.site = site
		self.data = self.connect.text
		self.url = self.connect.url
		self.headers = self.connect.headers
		self.status = STATUS[self.connect.status_code]