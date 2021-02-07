from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
import json
 
options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

chrome.get("https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")

time.sleep(1)

#抓取原始碼
html = chrome.page_source

soup = BeautifulSoup(html,'html.parser')

article_list = soup.select('article.MQsxIb')
# print(soup.prettify())

result = []

for article in article_list:
    #print(article)
    #select回傳會是list[],所以用select_one會是str
    link = article.select_one('.ipQwMb.ekueJc.RD0gLb a')
    
    media_name = soup.select_one('.wEwyrc.AVN2gc.uQIVzc.Sksgp').string
    title = link.string
    link_url = link.get('href')

    article_dict = {}
    article_dict['title'] = title
    article_dict['media_name'] = media_name
    article_dict['link_url'] = link_url 
    #print(article_dict)

    result.append(article_dict)
    pass

article_json = json.dumps(result, ensure_ascii=False) #中文字會不見，所以加上後面
# print(article_json)

with open('google新聞.json','wt', encoding='UTF-8') as file:
    file.write(article_json)

chrome.quit()
