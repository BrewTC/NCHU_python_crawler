from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
import json
 
options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

chrome.get("https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Frent.591.com.tw%2F%3Fkind%3D0%26region%3D8")

time.sleep(1)

#找到按下X鍵的id
chrome.find_element_by_id('area-box-close').click()

time.sleep(1)
#抓取原始碼
html = chrome.page_source

soup = BeautifulSoup(html,'html.parser')
#print(soup.prettify())

house_list = soup.select('.listBox .listInfo')
#print(house_list)

result = []

for house in house_list:
#     link = house.select_one('h3 a') 
#     #使用strip移除空白
#     link.string.strip()
#     #使用replace移除左右兩邊的空白
#     #title = link.string.replace(' ',' ').replace('\n',' '),replace('\r',' ')
#     link_url = link.get('href')
    
#     info = house.select('.lightBox')
#     info_box_1 = info[0].text.strip().replace

#     print(info_box_list_1)

#     pass

chrome.quit()