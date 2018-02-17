import requests

url = "http://www.baidu.com/s"
kv = {'wd':'python'}

r = requests.get(url,params = kv)
print(r.request.url)
r.raise_for_status()
print(len(r.text))