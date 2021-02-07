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

    #選擇一個大範圍出來
    ariticle_list = soup.select('.r-ent')


    #新增檔案
    #wt新增/會一直覆蓋掉舊的 ，a附加舊的資料上去   
    fp = open(directory_name+"/mydata.txt", "wt", encoding="UTF-8") 
    #若是亂碼要加後面的資料


    for i in ariticle_list:
        push_number = i.select_one('.hl')
        title = i.select_one('.title a')

        if title:
            if push_number:
                push_number_string = push_number.string
            else:
                push_number_string = 0
                
            title_string = title.string
            print(push_number_string, title_string)
            #寫入檔案
            fp.write(str(push_number_string) +" "+title_string+"\n")
            
        pass
    #關閉檔案
    fp.close()