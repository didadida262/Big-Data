import requests
from pyquery import PyQuery as pq

url = 'http://www.zhihu.com/explore'

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'	
}

html = requests.get(url,headers = headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()

for item in items:
	question = item.find('h2').text()
	author = item.find('.author-link-line').text()
	answer = pq(item.find('.content').html()).text()
	with open('explore.txt','a',encoding = 'utf-8') as f:
		f.write('\n'.join([question,author,answer]))
		f.write('\n' + '='*80 + '\n')
		

