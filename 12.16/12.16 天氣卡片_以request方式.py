import requests
from bs4 import BeautifulSoup

r = requests.get('https://shes40633.github.io/weather/')

# 判斷伺服器回應的狀態碼，如果是在200-299的區間（成功回應）
if r.status_code >=200 and r.status_code <=299:
    # print(r.text) #取得網頁原始碼
    # 以 Beautiful Soup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')

    print(soup.prettify())