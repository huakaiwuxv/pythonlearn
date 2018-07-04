from selenium import webdriver
from lxml import etree
import time

driver=webdriver.PhantomJS()
driver.maximize_window()

def get_info(url,page):
    page=page+1
    driver.get(url)
    driver.implicitly_wait(10)
    selector=etree.HTML(driver.page_source)
    with open('hello.html','w',encoding='utf-8')as f:
        f.write(driver.page_source)
    infos=selector.xpath()


    if page<=50:
        NextPage(url,page)
    else:
        pass

def NextPage(url,page)
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('').click
    time.sleep(4)
    get_info(driver.current_url,page)

if __name__=="__main__":
driver.get(url)
driver.implicitly_wait(10)
driver.find_element_by_id('q').clear
driver.find_element_by_id('q').send_keys('男士短袖')
driver.find_element_by_class_name('btn-search').click()
get_info(dr .current_url,1)