# -*- coding: UTF-8 -*-
import requests
from urllib import parse
from urllib.request import urlretrieve
import os
from bs4 import BeautifulSoup
import re
import json
import ssl
 
# This restores the same behavior as before.
context = ssl._create_unverified_context()

# 报名青年大学习
data = {
    "Level1options": os.environ['Level1options'],
    "Level2options": os.environ['Level2options'],
    "Level3options": os.environ['Level3options'],
    "Level4options": os.environ['Level4options'],
    "name": os.environ['name'],
}

url = "http://gsqndxx.gsjiahua.com.cn/inserts?" + parse.urlencode(data)

res = requests.post(
    url, headers={"Content-Type": "application/x-www-form-urlencoded"})

print(url)
print(res.text)

# 提取url
# res_url = requests.get('https://news.cyol.com/gb/channels/vrGlAKDl/')
# bs_url = BeautifulSoup(res_url.text, 'html.parser')
# list_url = bs_url.find_all('ul', class_='movie-list')
# tag_a = list_url[0].find('a')
# url = str(tag_a)
# matchObj = re.match(r'<a class="transition" href="https://h5.cyol.com/special/daxuexi/(.+)/index.html', url)
# identifier = matchObj.group(1)
# img_url = 'https://h5.cyol.com/special/daxuexi/' + identifier + '/images/end.jpg'

# 推送结果及截图
img_name = "screenshot"
urlretrieve(img_url, 'screenshot.jpg')
token = os.environ['PPTOKEN']
title = '自动大学习'
content = '本期青年大学习已完成' # ，截图已经生成\n' + img_url

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 "
                  "Mobile Safari/537.36",
    'Content-Type': 'application/json'
}
url = 'http://www.pushplus.plus/send'
data = {'token': token, 'title': title, 'content': content, 'template': 'html'}
res = requests.post(headers=headers, url=url, data=json.dumps(data), timeout=10)
print(res.text)
