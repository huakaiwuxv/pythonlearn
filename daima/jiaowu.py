import requests
import re
from bs4 import BeautifulSoup
#from lxml import etree
#import time
headers={
    'accept':'*/*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
for i in range(1,3):
    urls={'http://zhjw.hbu.edu.cn'}

    photos=[]
    for url in urls:
        wb_data=requests.get(url,headers=headers)
        soup=BeautifulSoup(wb_data.text,'lxml')
        
        
        imgs=soup.select('#vchart')#vchart
        for img in imgs:
            photo=img.get('src')
            photos.append(photo)
    path="F://jiaowu/"
    abc=".jpg"
    for item in photos:
        data=requests.get(item,headers=headers)
    # https://passport.lagou.com/vcode/create?from=register&amp;refresh=3
    #src="https://passport.lagou.com/vcode/create?from=register&amp;refresh=1"
        #photo_name=re.findall('\/vcode\/(*?*=*&*;*=d)\d',item)
        #/validateCodeAction.do?random=0.920194857932022
        photo_name=re.findall('\/(.*)\?',item)
        photo_name=photo_name
        print(photo_name)
        
        

        str_num = str(i)
        if photo_name:
            fp=open(path+photo_name[0]+str_num+abc,'wb')
            print(path+photo_name[0])
            fp.write(data.content)
            fp.close()     