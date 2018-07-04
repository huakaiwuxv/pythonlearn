import requests
import re
from bs4 import BeautifulSoup
#from lxml import etree
#import time
headers={
    'accept':'*/*',
    'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
for i in range(1,2):
    urls={'http://passport2.chaoxing.com/login?fid=&refer='}
    #urls={'https://passport.zhaopin.com/org/login?DYWE=1523588074950.410101.1523588075.1523588075.1'}
    #urls={'https://www.pexels.com/?page={}'.format(str(i)) for i in range(1,2)}
    photos=[]
    for url in urls:

    #for num in range(1,20):  # 迭代 10 到 20 之间的数字
        wb_data=requests.get(url,headers=headers)
        soup=BeautifulSoup(wb_data.text,'lxml')
        #time.sleep(10)
        #driver.find_element_by_class_name('yzm').click()
        #driver.find_element_by_class_name('reflash').click()
        
    #phone_form > ul > li.yzmli > img
        imgs=soup.select('#numVerCode')#phone_form > ul > li.yzmli > a
        #phone_form > ul > li.yzmli > img
        for img in imgs:
            photo=img.get('src')
            photos.append(photo)
    path="F://ph/"
    abc=".jpg"
    for item in photos:
        data=requests.get(item,headers=headers)
    # https://passport.lagou.com/vcode/create?from=register&amp;refresh=3
    #src="https://passport.lagou.com/vcode/create?from=register&amp;refresh=1"
        #photo_name=re.findall('\/vcode\/(*?*=*&*;*=d)\d',item)
        #photo_name=re.findall('\/vcode\/create\?from=register&amp;refresh\=(*)\d',item)
        photo_name=re.findall('refresh\=(.*\d)\d',item)
        photo_name=photo_name
        print(photo_name)
        
        

        str_num = str(i)
        if photo_name:
            fp=open(path+photo_name[0]+str_num+abc,'wb')
            print(path+photo_name[0])
            fp.write(data.content)
            fp.close()
    
      