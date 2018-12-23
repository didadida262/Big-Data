import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool



def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd':'synthesis'

    }

    base_url = 'https://www.toutiao.com/search_content/?'
    url = base_url + urlencode(params)

    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None
    except requests.ConnectionError:
        return None

def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield{
                'title':title,
                'image':'http:' + image.get('url')
                }


def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('image'))
        if resp.status_code == 200:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name = md5(resp.content).hexdigest(),
                file_suffix = 'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(resp.content)
		                     
    except requests.ConnectionError:
            print('Failed to Save Image，item %s' % item)

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        save_image(item)

GROUP_START = 0
GROUP_END = 7
  

if __name__ == '__main__':
    pool = Pool()
    groups = ([x*20 for x in range(GROUP_START,GROUP_END + 1)])
    pool.map(main,groups)
    pool.close()
    pool.join()