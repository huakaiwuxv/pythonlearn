import urllib.request  
req=urllib.request.urlopen('http://www.imooc.com/course/list')  
buf=req.read()  
#显示从网页上抓取到的内容  
buf  
#通过正则表达式获取图片地址  
import re  
#本人用的是python3.5，直接用findall会出错，因此需要下面一句对buf进行编码  
buf=buf.decode('UTF-8')  
#//img3.mukewang.com/5ac2dec100014aae05400300-240-135.jpg
listurl=re.findall(r'src=.+\.jpg',buf)  
listurl=re.findall(r'http:.+\.jpg',buf)#显示图片的网址  
listurl  
#将图片写入本地  
i=0  
for url in listurl:  
     f=open(r"F:\\ph"+'/'+str(i)+'.jpg','wb')  
     req=urllib.request.urlopen(url)  
     buf=req.read()  
     f.write(buf)  
     i+=1 