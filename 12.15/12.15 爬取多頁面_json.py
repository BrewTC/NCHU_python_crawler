# ptt 股票版 / title / 推文數

# 引入模組
import requests
from bs4 import BeautifulSoup
import os
import json

results = []
temp_list=[]

def make_directory():
    # 建立資料夾
    directory_name = "1214_data"

    # 是否有這個資料夾存在，如果不存在 就建立一個新的資料夾
    if not directory_name in os.listdir(): #true or false
        os.mkdir(directory_name)
    
    return directory_name

def get_page_url(p=10):
    # 使用 GET 方式下載普通網頁
    r = requests.get('https://www.ptt.cc/bbs/Stock/index.html')

    # 判斷伺服器回應的狀態碼，如果是在200-299的區間（成功回應）
    if r.status_code >=200 and r.status_code <=299:
        # print(r.text) #取得網頁原始碼
        # 以 Beautiful Soup 解析 HTML 程式碼
        soup = BeautifulSoup(r.text, 'html.parser')

        btn_list = soup.select('.btn.wide')
        previous_page = btn_list[1].get('href').split('/')[-1]
        page_number = previous_page.replace("index", "").replace(".html", "")
        # print(page_number)
        # 4998

        page_url_list = ['https://www.ptt.cc/bbs/Stock/index.html']

        for i in range(p):
            # print(int(page_number) - i)
            url = "https://www.ptt.cc/bbs/Stock/index{}.html".format(int(page_number) - i)
            page_url_list.append(url)
            pass

        # for url in page_url_list:
        #     print(url)
        #     pass

        return page_url_list

def get_one_page_data(url):
    # 使用 GET 方式下載普通網頁
    r = requests.get(url)

    # 判斷伺服器回應的狀態碼，如果是在200-299的區間（成功回應）
    if r.status_code >=200 and r.status_code <=299:
        # print(r.text) #取得網頁原始碼
        # 以 Beautiful Soup 解析 HTML 程式碼
        soup = BeautifulSoup(r.text, 'html.parser')

        ariticle_list = soup.select('.r-ent')

        for i in ariticle_list:
            push_number = i.select_one('.hl')
            title = i.select_one('.title a')
        
            if title:
                date = i.select_one('.meta .date').string
                author = i.select_one('.author').string
                link = title.get('href')

                if push_number:
                    push_number_string = push_number.string
                else:
                    push_number_string = "0"
                    
                title_string = title.string

                article = {}
                article['push_number'] = push_number_string
                article['title'] = title_string
                article['link'] = link
                article['author'] = author #作者
                article['date'] = date

                temp_list.append(article)

                # print(results)
                
            pass

#main
#建立資料夾，並回傳資料夾目錄名稱
directory_name = make_directory()

#取得首頁以及後10頁的網址，回傳list
url_list = get_page_url(p=5)

#依每個網址去爬取資料，將資料存放至results(list)
for url in url_list:
    # print(url)
    temp_list=[]
    get_one_page_data(url=url)
    temp_list.reverse()

    for i in temp_list:
        results.append(i)
    pass

#將results轉存成JSON並匯出成一份txt
print(results)

article_json = json.dumps(results, ensure_ascii=False)
print(article_json)

#with語句來自動幫我們呼叫close()方法，不用再寫file.close()
with open('123.txt', 'wt', encoding='UTF-8') as file: #wt(write text(一般文字用))
    file.write(article_json)