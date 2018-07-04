import requests

url='http://baidu.com'
r=requests.get(url,timeout='1')
print(r.text)