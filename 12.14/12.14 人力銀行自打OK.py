import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.104.com.tw/cust/list/index/?page=1&order=1&mode=s&jobsource=checkc')
#print(r.status_code)

#status_code:HTTP狀態碼
if r.status_code >=200 and r.status_code <= 299:
    # print(r.text)
    soup = BeautifulSoup(r.text,'html.parser')
    #print(soup.prettify())
    #先切出大的項目
    article_list = soup.select('article')
    #print(article_list)
    for article in article_list:
    #取得大標題,只選一個
        title = article.select_one('.info h1 a')
        print(title.string)

    pass