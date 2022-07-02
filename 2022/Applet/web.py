import webbrowser
import requests

def search(kw,se = 'https://cn.bing.com/search?q=%s'):
    url = se % kw
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',}
    response = requests.get(url=url, headers=headers)
    fileName = 'Cache.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    webbrowser.open(fileName)
    return 0;

def web(url,*arg):
    '/'.join(url,*arg)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',}
    response = requests.get(url=url, headers=headers)
    fileName = 'Cache.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    webbrowser.open(fileName)
    return 0;