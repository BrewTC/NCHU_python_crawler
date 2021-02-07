#多筆資料 ->列表(list) , 詳細的屬性 -> 字典(dict)
import json
import csv
import sys

article = {}
article['post_number'] = '爆'
article['title'] = 'Re: [請益] 把無本當沖當事業的人頭腦在想甚麼?'

article1 = {}
article1['post_number'] = '33'
article1['title'] = '[公告] Stock 股票板板規 V3 (檢舉洽 yoche2000)'

article2 = {}
article2['post_number'] = '0'
article2['title'] = '[閒聊] 2020/12/15 盤中閒聊'

article_list=[]
article_list.append(article)
article_list.append(article1)
article_list.append(article2)

# article_json = json.dumps(article_list, ensure_ascii=False)
# print(article_json)

# with open('123.txt', 'wt', encoding='UTF-8') as file:
#     file.write(article_json)

with open("data.csv", "w",encoding='utf-8-sig') as file:
    csv_file = csv.writer(file)
    #表頭
    csv_file.writerow(['推文數','標題'])
    #內容
    for article in article_list:
        csv_file.writerow([article['post_number'], article['title']])