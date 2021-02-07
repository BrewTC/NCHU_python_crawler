#youtube_頁面捲動
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time

options = Options()
#增加chrome啟用參數(可以跳過禁用擴充)
options.add_argument("--disable-notifications")
#物件宣告(Chrome)
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)


#前往至某個網頁
chrome.get("https://www.youtube.com/?gl=TW&tab=w1")

#停止三秒
time.sleep(3)

for i in range(3):
    #在當前框架中執行JavaScript指令碼  
    # #(execute_script(script, JS指令碼))
    chrome.execute_script('window.scrollTo(0, document.querySelector("ytd-app").clientHeight);')  # 重複往下捲動
    time.sleep(3)
    pass

#抓取原始碼
html = chrome.page_source

#解析
soup = BeautifulSoup(html,'html.parser')
#print(soup.prettify())

title_list = soup.select('#video-title.ytd-rich-grid-media')

for title in title_list:
    print(title.string)
    pass

#關閉
chrome.quit()