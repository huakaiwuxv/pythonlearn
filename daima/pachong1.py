import requests
import re
from bs4 import BeautifulSoup
headers={
    'accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
urls={'https://www.pexels.com/?page={}'.format(str(i)) for i in range(1,2)}
photos=[]
for url in urls:
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text,'lxml')
    imgs=soup.select('body > div.l-container.home-page > div.photos > article > a.js-photo-link > img')
    for img in imgs:
        photo=img.get('src')
        photos.append(photo)
path="F://photo/"
for item in photos:
    data=requests.get(item,headers=headers)
    #https://images.pexels.com/photos/129459/pexels-photo-129459.jpeg?auto=compress&cs=tinysrgb&h=350
    photo_name=re.findall('\/\d+\/(.*?)\?',item)
    print(photo_name)
    if photo_name:
        fp=open(path+photo_name[0],'wb')
        print(path+photo_name[0])
        fp.write(data.content)
        fp.close()
    
      