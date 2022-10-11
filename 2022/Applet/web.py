import webbrowser
import requests
baidu = "baidu.com/s?wd="
bing = "bing.com/search?q="
google = "google.com/search?q="


class Client(object):
    def __init__(self):
        self.site = "about:blank"
    def open(self):
        webbrowser.open(self.site)
    def search(self,kw):
        webbrowser.open(self.site+kw)
    def setsite(name):
        self.site = name
    @property
    def clear(self):
        self.site = "about:blank"
        return 0