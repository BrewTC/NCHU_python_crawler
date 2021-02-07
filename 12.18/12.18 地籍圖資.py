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
chrome.get("https://easymap.land.moi.gov.tw/R02/Index#")

#門牌
chrome.find_element(By.ID, "button_addr").click()
#選縣市
select_city = Select(chrome.find_element(By.ID, "select_city_id1"))
select_city.select_by_visible_text("臺中市")

time.sleep(3)

select_town = Select(chrome.find_element(By.ID, "select_town_id1"))
select_town.select_by_visible_text("南區")

time.sleep(1)

select_road = Select(chrome.find_element(By.ID, "select_road_id"))
select_road.select_by_visible_text("學府路")

time.sleep(1)

chrome.find_element(By.ID, "doorNoId").send_keys("64")
chrome.find_element(By.ID, "door_botton").click()

time.sleep(3)

html = chrome.page_source

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

result_table = soup.select_one('#one-column-emphasis')
# print(result_table)

headers = result_table.select('th')
contents = result_table.select('td')

def remove_html(element):
    return element.string

headers = list(map(remove_html, headers))
contents = list(map(remove_html, contents))

# print(headers)
# print(contents)

with open("地圖圖資.csv", "w",encoding='utf-8-sig') as file:
    csv_file = csv.writer(file)

    #表頭
    csv_file.writerow(headers)
    
    #內容
    csv_file.writerow(contents)

#只做一筆table，轉成csv不用for

chrome.quit()