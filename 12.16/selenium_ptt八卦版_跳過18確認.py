from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
 
options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

#以附加cookie的方式
chrome.get("https://www.ptt.cc/bbs/Gossiping/index.html")

chrome.add_cookie({"name": "over18", "value": "1"})

chrome.get("https://www.ptt.cc/bbs/Gossiping/index.html")

# 直接模擬按下按鈕的方式
# chrome.find_element_by_name("yes").click()