import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

r = requests.get('https://www.taiwan.net.tw/m1.aspx?sNo=0001112')

result = []

if r.status_code >=200 and r.status_code <=299:
    # print(r.text) #取得網頁原始碼
    # 以 Beautiful Soup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')

    card_list = soup.select('.card')
    
    for card in card_list:

        title = card.select_one('.card-title').string
        img_url = card.select_one('.graphic img.lazyload').get('data-src')
        people_count = card.select_one('.target-like').text.replace('瀏覽人次：','')
        
        hashtag_list = card.select('.hashtag a')
        hashtag_final_list=[] 
        for hashtag in hashtag_list:
            hashtag_final_list.append(hashtag.string)
            pass
        
        link_url = card.select_one('.card-link').get('href')

        card_dict = {}
        card_dict['title'] = title
        card_dict['img_url'] = img_url
        card_dict['people_count'] = people_count
        card_dict['hashtag'] = hashtag_final_list
        card_dict['link_url'] = link_url

        result.append(card_dict)
        pass

#print(result)
card_json = json.dumps(result, ensure_ascii=False)


#輸出成json
with open('交通部觀光局景點資訊.json', 'wt', encoding='UTF-8') as file:
    file.write(card_json)
print(card_json)

#抓取json檔案 再轉存成csv
df = pd.read_json ('交通部觀光局景點資訊.json')
new_header = ['景點名稱', '景點圖片連結', '閱讀人數', 'hashtag', '內頁連結'] 
export_csv = df.to_csv ('交通部觀光局景點資訊.csv', index = None, header=new_header,encoding='utf-8-sig')