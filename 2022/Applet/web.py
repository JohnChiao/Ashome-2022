import webbrowser
import requests

def search():
    kw = input('Search')
    url = 'https://www.google.com/search?q=' + kw
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',}
    response = requests.get(url=url, headers=headers)
    fileName = '__pycache__/webcache.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    webbrowser.open(fileName)


def web(url,*arg):
    '/'.join(url,*arg)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',}
    response = requests.get(url=url, headers=headers)
    fileName = 'Cache.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    webbrowser.open(fileName)
    return 0;