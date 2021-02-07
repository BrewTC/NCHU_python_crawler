# request套件
# BeautifulSoup套件
#HTTP 狀態碼
import requests #引入requests模組
from bs4 import BeautifulSoup

item = input()
my_params = {'q':item}

r = requests.get('https://www.google.com.tw/' , params = my_params)
#伺服器回應的狀態碼 200~299, 404/500 ->fail
print(r.status_code) #200
print(type(r.text))

#判斷伺服器回應的狀態碼，如果是在200~299區間(成功回應)
# if r.status_code >=200 and r.status_code <= 299:
    #print(r.text) #取得網頁原始碼
    # soup = BeautifulSoup(r.text,'html.parser')
    # print(soup)
