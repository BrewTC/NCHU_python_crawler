from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

#前往至某個網站
chrome.get("https://dinbendon.net/do/login;jsessionid=1E5365E6F52721BE075D814AF8F5A046")

#取得表單內的某一個input element，透過name
chrome.find_element_by_name('username').send_keys("Hanks")
chrome.find_element_by_name('password').send_keys("123456789")

qestion = chrome.find_elements_by_class_name("alignRight")[-1].text
temp = re.findall(r"\d+\.?\d*", qestion)
total = int(temp[0])+int(temp[1])

chrome.find_element_by_name('result').send_keys(total)

chrome.find_element_by_name("submit").click()