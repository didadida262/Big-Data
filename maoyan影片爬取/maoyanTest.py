import requests
import json
import re
import time
from requests.exceptions import RequestException


def get_one_page(url):
	try:
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
		response = requests.get(url,headers = headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parse_one_page(html):
	pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'	#获取名词
		                   + '.*?data-src="(.*?)"'			#获取图片
		                   + '.*?name.*?a.*?>(.*?)</a>'		#获取名称
		                   + '.*?star">(.*?)</p>'			#获取演员
		                   + '.*?releasetime">(.*?)</p>'	#获取发布时间
		                   + '.*?integer">(.*?)</i>'		#获取分数整数部分及小数点
		                   + '.*?fraction">(\d)</i>.*?</dd>',re.S)	#获取分数小数部分
	items = re.findall(pattern,html)
	for item in items:			#生成一个字典
		yield{
			'index':item[0],
			'image':item[1],
			'name':item[2],
			'actors':item[3].strip()[3:],
            'releasetime':item[4].strip()[5:],
			'score':item[5].strip() + item[6].strip()
		}

def write_to_file(content):
	with open('result.txt','a',encoding='utf-8') as f:
		f.write(json.dumps(content,ensure_ascii=False)+'\n')


def main(offset):
	url = 'http://maoyan.com/board/4?offset=' + str(offset)
	html = get_one_page(url)
	for haha in parse_one_page(html):
		print(haha)
		write_to_file(haha)


if __name__ == "__main__":
	for i in range(10):
		main(offset=i*10)
		time.sleep(0.1)

