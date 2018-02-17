import requests
import os

url = "http://www.sju.edu.cn/_upload/article/images/39/ff/3449b19c495daeb7ed4401860075/db4df06f-0172-4ee9-bcdd-c82717d96015.jpg"
root = "G://python//爬虫系列//图片爬去//"
path = root + url.split('/')[-1]

try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else:
		print("文件已存在")
except:
	print("爬去失败")