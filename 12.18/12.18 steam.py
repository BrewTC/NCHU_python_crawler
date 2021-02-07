from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv
#利用selenium IDE 抓取到網頁上的選取路徑

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

#前往至某個網址
chrome.get("https://store.steampowered.com/app/1091500/Cyberpunk_2077/")

#還沒解決好如何跳過生日
chrome.find_element_by_id('age_gate_btn_continue').click()

time.sleep(3)

#捲動畫面
for i in range(3):
    chrome.execute_script('documentElement.scrollTop=999999')
    time.sleep(3)
    pass

#取得網頁原始碼
html = chrome.page_source
soup = BeautifulSoup(html,'html.parser')
#print(soup.prettify())

card_list = soup.select('.apphub_Card')

for card in card_list:
    author = card.select_one('apphub_cardContentAuthorName').text
    contents = card.select_one('apphub_cardTextContent').text
    post_time = card.select