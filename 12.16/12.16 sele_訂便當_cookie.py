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

time.sleep(1)

chrome.add_cookie({"name": "signInPanel__signInForm__username", "value": "Hanks"})
chrome.add_cookie({"name": "signInPanel__signInForm__password", "value": "P2VLbVENq8M4r%2FytyItB1w%3D%3D"})
#密碼好像會失效
chrome.add_cookie({"name": "JSESSIONID", "value": "021691DDB61F24BFF2361A0D986A321A"})

time.sleep(1)

chrome.refresh()