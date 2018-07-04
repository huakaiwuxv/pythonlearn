import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import etree
import time
driver=webdriver.PhantomJS()
driver.maximize_window()
headers={
    'accept':'*/*',
    'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
url={'https://www.lagou.com/lp/html/common.html?utm_source=m_cf_cpt_baidu_pc'}
#urls={'https://passport.zhaopin.com/org/login?DYWE=1523588074950.410101.1523588075.1523588075.1'}
#urls={'https://www.pexels.com/?page={}'.format(str(i)) for i in range(1,2)}
photos=[]
#for url in urls:

   # driver.get(url)
    #driver.implicitly_wait(10)
    #driver.find_element_by_id('q').clear
    #driver.find_element_by_id('q').send_keys('男士短袖')
    #driver.find_element_by_class_name('btn-search').click()
    #driver.find_element_by_class_name('lgn-verbtn').click()

   # get_info(dr .current_url,1)
    
wb_data=requests.get(url,headers=headers)
driver.get(url)
for num in range(1,20):  # 迭代 10 到 20 之间的数字
    soup=BeautifulSoup(wb_data.text,'lxml')
    driver.implicitly_wait(10)
    #driver.find_element_by_class_name('yzm').click()
    driver.find_element_by_class_name('reflash').click()
#phone_form > ul > li.yzmli > img
    imgs=soup.select('#phone_form > ul > li.yzmli > img')
    for img in imgs:
        photo=img.get('src')
        photos.append(photo)
path="F://ph/"
for item in photos:
    data=requests.get(item,headers=headers)
   # https://passport.lagou.com/vcode/create?from=register&amp;refresh=3
    photo_name=re.findall('\/vccode\/(.*?)\?',item)
    print(photo_name)
    if photo_name:
        fp=open(path+photo_name[0],'wb')
        print(path+photo_name[0])
        fp.write(data.content)
        fp.close()
    
      