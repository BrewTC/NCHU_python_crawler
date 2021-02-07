#先安裝BeautifulSoup、requests模組
from bs4 import BeautifulSoup
import requests

#使用get方式取得普通網頁
r = requests.get("https://www.ptt.cc/bbs/Stock/index.html")
print(r) 
#<Response [200]>

html_code = ""

#status_code == 200取得伺服器傳回的狀態碼
if r.status_code == 200:
    html_code = r.text #用text就可以取得網頁HTML原始碼
    soup = BeautifulSoup(html_code, 'html.parser')
    pass

#print(soup.prettify())

#去蕪存菁，先去網路上面檢查
titile_lists = soup.select('div,r-ent div.title a')
for a in titile_lists:
    #輸出超連結文字
    print(a)

    #動態載入，是不一樣的爬蟲方式，用模擬器的方式下載資源

    a_list = soup.select('div.r_ent')
    #print(a_list)
# for a in a_list:
    #輸出超連結的文字

    #內容
    # number_of_hot = a.find("span",class_="h1")
    # if number_of_hot != '':
    # print(number_of_hot)