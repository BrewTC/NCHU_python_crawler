import requests
from bs4 import BeautifulSoup

def get_one_page_data():
    from bs4 import BeautifulSoup
    url = 'https://www.ptt.cc/bbs/Stock/index4998.html'
    r = requests.get(url)

    if r.status_code >=200 and r.status_code <= 299:
    #print(r.text)
        soup = BeautifulSoup(r.text,'html.parser')
    #印出排版過的HTML原始碼

    #去無存菁
    #find:一個,find all:多個
    #select:多個,select_one:一個

    #原本錯誤的做法
    #   x_list = soup.select('.h1')
    # for i in x_list:
    #     print(i)
    # y_list = soup.select('.title')
    # for i in y_list
    #     print(i)

    #正確的作法:由外而內，先挑選大的，再進到裡面的項目
        ariticle_list = soup.select('.r-ent')    #先篩出大範圍
    #如果是使用select,出來會是list,這樣出來要再做一次for的處理,用select_one
        for i in ariticle_list:
            push_number = i.select_one('.hl')
            title = i.select_one('.title a')

            if title:
                if push_number: 
                    push_number_string = push_number.string
                else:
                    push_number_string = 0

                title_string = title.string
            else:    
                print(push_number_string, title_string)
        pass




