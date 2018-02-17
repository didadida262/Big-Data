import requests

url = "https://www.icourse163.org/home.htm?userId=5477000#/home/course"
try:
	kv = {'user-agent':'Mozilla/5.0'}
	#隐藏自己爬虫的身份
	r = requests.get(url,header = kv)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:20000])
except:
	print("爬去失败")



