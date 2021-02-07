import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 使用 GET 方式下載普通網頁
r = requests.get('https://shes40633.github.io/weather/')

# 判斷伺服器回應的狀態碼，如果是在200-299的區間（成功回應）
if r.status_code >=200 and r.status_code <=299:
    # print(r.text) #取得網頁原始碼
    # 以 Beautiful Soup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup.prettify())

options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)


#前往至某個網頁
chrome.get("https://shes40633.github.io/weather/")

#停止三秒
time.sleep(3)

#抓取原始碼
html = chrome.page_source

#解析
soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())


chrome.quit()

