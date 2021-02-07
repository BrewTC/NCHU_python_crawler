#先抓網站上面的上一頁按鈕


# ptt 股票版 / title / 推文數
import requests
from bs4 import BeautifulSoup
import os

#建立資料夾
directory_name = "1214_data"

# 是否有這個資料夾存在，如果不存在 就建立一個新的資料夾
if not directory_name in os.listdir(): #true or false
    os.mkdir(directory_name)

# 使用 GET 方式下載普通網頁
r = requests.get('https://www.ptt.cc/bbs/Stock/index4998.html')

# 判斷伺服器回應的狀態碼，如果是在200-299的區間（成功回應）
if r.status_code >=200 and r.status_code <=299:
    # print(r.text) #取得網頁原始碼
    # 以 Beautiful Soup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')

    ariticle_list = soup.select('.btn.wide')







    btn_list = soup.select('.btn.wide')

    #print(btn_list) #索引值[2],是上一頁,選2

    #取得html特定屬性的數值
    #print(btn_list[1].get('href'))
    #/bbs/Stock/index4997.html

    #print(btn_list[1].get('href').split('/'))
    #['', 'bbs', 'Stock', 'index4997.html']

    previous_page = btn_list[1].get('href').split('/')[-1]
    page_number = previous_page.replace("index", "").replace("html","")

    page_url_list = ['https://www.ptt.cc/bbs/Stock/index4998.html']

    for i in range(10):
        #print(int(page_number) -i)
        url = "https://www.ptt.cc/bbs/Stock/index{}.html".format(int(page_number) -i)
        page_url_list.append(url)
        pass
    for url in page_url_list:
        print(url)
        pass