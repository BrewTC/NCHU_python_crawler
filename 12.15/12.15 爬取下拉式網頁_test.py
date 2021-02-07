from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from  bs4 import BeautifulSoup
import time
 
 
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
#前往至某個網頁
chrome.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone")

#停止3秒
time.sleep(3)
#抓取原始碼
html = chrome.page_source
#解析
soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())
#關閉，二選一即可
#chrome.close()
chrome.quit()