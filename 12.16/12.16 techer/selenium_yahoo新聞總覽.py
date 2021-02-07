from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
 
options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

#前往至某個網址
chrome.get("https://tw.news.yahoo.com/archive")

# 停止3秒
time.sleep(2)

#捲動
for i in range(3):
    chrome.execute_script('window.scrollTo(0, 999999999);')  # 重複往下捲動
    time.sleep(3)
    pass

# 抓取原始碼
html = chrome.page_source

# 解析
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())    

article_list = soup.select(".StreamMegaItem")

for article in article_list:
    image = article.select_one('img')
    
    if image:
        title = image.get('alt')
        img_url = image.get('src')

        response = requests.get(img_url)

        title = title.replace('/','-')

        with open("img_data/{}.png".format(title), "wb") as file:
            file.write(response.content)

    pass


# 關閉
chrome.quit()