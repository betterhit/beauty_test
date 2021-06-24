import requests
import time
from bs4 import BeautifulSoup
import json
import re
numdict = {}
'''
def get_youmei():
    count = 0
    url = "https://www.umei.net/meinvtupian/meinvxiezhen/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'}
    resp = requests.get(url=url, headers=headers)
    #获得美女写真主页面源代码
    resp.encoding = 'utf-8'
    main_page = BeautifulSoup(resp.text,"html.parser")
    alist = main_page.find("div",class_="TypeList").find_all("a")
    i=0
    for a in alist:
        href ="https://www.umei.net"+a.get('href')
        #获得的子页面的额网址并不完整，需要补充前缀，否则无法打开
        child_resp = requests.get(url=href, headers=headers)
        child_resp.encoding = 'utf-8'
        child_page = BeautifulSoup(child_resp.text,"html.parser")
        child_img = child_page.find("div",class_="ImageBody").find("img").get('src')
        #得到高清大图的网址
        img = requests.get(url=child_img, headers=headers)
        #请求高清大图的网址进行下载
        img_name = child_img.split("/")[-1]
        #以分割线的末尾命名
        with open('C:/Users/fuhang/Desktop/beauty/'+str(i)+'.jpg','wb') as f:
            f.write(img.content)
            i+=1
        print("over!!!",img_name)
        time.sleep(1)
        count+=1
        if count >5:
            break
    print("all over!!!")
'''
def get_huya():
    count = 0
    url = "https://www.huya.com/g/2168"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'}
    resp = requests.get(url=url, headers=headers)
    # 获得虎牙主页面源代码
    resp.encoding = 'utf-8'
    main_page = BeautifulSoup(resp.text, "html.parser")
    datalist = main_page.find_all("li")

    for data in datalist:
        src = data.find("img",class_ = 'pic').get('data-original')
        img = requests.get(url=src, headers=headers)
        # 请求高清大图的网址进行下载
        img_name = data.find("i", class_="nick").get('title')
        # 以分割线的末尾命名
        m = data.find("i",class_="js-num")
        obj = re.compile(r'<i.*?class="js-num">(?P<num>.*?)</i>',re.S)
        nmum = obj.finditer(str(m))
        for i in nmum:

            numdict[img_name]=i.group('num')
        with open('C:/Users/fuhang/Desktop/huya/' + img_name + '.jpg', 'wb') as f:
            f.write(img.content)
        print("over!!!", img_name)
        count+=1
        time.sleep(1)
        if count>5:
             break
    print("all over!!!")
def get_douyu():
    url = "https://m.douyu.com/api/room/list?page=1&type=dance"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'}
    resp = requests.get(url=url, headers=headers)
    # 获得斗鱼主播封面的文件网址
    resp.encoding = 'utf-8'
    datalist = json.loads(resp.text)['data']
    #加载为json文件方便解析
    for i in range(0,8):
        src = datalist['list'][i]['verticalSrc']
        temp = datalist['list'][i]['hn']
        img = requests.get(url=src, headers=headers)
        img_name = datalist['list'][i]['nickname']
        numdict[img_name] = temp
        with open('C:/Users/fuhang/Desktop/douyu/' + img_name + '.jpg', 'wb') as f:
            f.write(img.content)
        print("over!!!", img_name)
        time.sleep(1)

get_huya()
get_douyu()
