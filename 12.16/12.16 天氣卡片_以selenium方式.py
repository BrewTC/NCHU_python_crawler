from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
 
options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

#前往至某個網址
chrome.get("https://shes40633.github.io/weather/")

# 停止3秒
time.sleep(3)

# 抓取原始碼
html = chrome.page_source

# 解析
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

# card_list = soup.select('.weather_card')

# for card in card_list:
#     area = card.select_one('.area').string
#     temperature = card.select_one('.temperature').string

#     print(area,temperature)
#     pass

# # 關閉
# chrome.quit()