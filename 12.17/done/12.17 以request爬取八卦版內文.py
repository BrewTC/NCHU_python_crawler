import requests
from bs4 import BeautifulSoup

cookies = {'over18': '1'}

r = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies=cookies)

if r.status_code >=200 and r.status_code <=299:
    # print(r.text) #取得網頁原始碼
    # 以 Beautiful Soup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')

    # print(soup.prettify())

    article_list = soup.select('.r-ent')

    articel_result = []

    for i in article_list:
            #推文數
            push_number = i.select_one('.hl')
            #標題
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
                article['author'] = author
                article['date'] = date
                articel_result.append(article)
            pass

# print(articel_result)

# 取得個別頁面的內容
for article in articel_result:
    print(article['link'])
    r = requests.get('https://www.ptt.cc'+article['link'], cookies=cookies)
    if r.status_code >=200 and r.status_code <=299:
        # print(r.text) #取得網頁原始碼
        # 以 Beautiful Soup 解析 HTML 程式碼
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.prettify())

        content = soup.select_one('#main-content')

        title = article['title'].replace('/','-')
        
        with open('data/{}.txt'.format(article['title']),'wt',encoding='UTF-8') as file:
            file.write(content.text)
        #後面有點跑不順?
    pass