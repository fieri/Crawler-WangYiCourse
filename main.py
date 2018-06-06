# coding=utf-8
import requests
import codecs
import os.path
import os
from bs4 import BeautifulSoup
import re
import platform
import wget

url = 'http://yipeiwu.com/getvideo.html'

parameter = {
    "url":"http://open.163.com/special/sp/introductiontopsychology.html"
}

parameter['url'] = input("输入要下载的网址：")
savedir = input("请输入要保存的路径：")

if(not os.path.exists(savedir)):
    os.makedirs(savedir) 


res = requests.get(url,params = parameter,timeout=10)

while res.status_code!=200:
    print ('retrying...')
    res = requests.get(url,params = parameter,timeout=50)
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text,'html.parser')
contents = soup.find_all('a',id="downloadVideo2")

for content in contents:
    #print(content)
    href = content["href"]
    title = content.parent.parent.find("th").text
    #print(href+" "+title)

    title = title.replace(":","").replace("\\","").replace("/","").replace("?","").replace("*","").replace("\"","").replace("<","").replace(">","").replace("|","")
    if (platform.system() =="Windows"):
        savepath = os.path.join(savedir, title+".mp4")
        # savepath = "f://耶鲁大学公开课：心理学导论//"+title+".mp4"
    elif (platform.system() =="Linux"):
        savepath = '/home/Downloads/AiEasyVideo'
    
    
    if not os.path.exists(savepath):
        print("正在下载："+savepath)
        r = requests.get(href) # create HTTP response object

        with open(savepath,'wb') as f:
            f.write(r.content)
    else:
        print("下载成功："+savepath)
