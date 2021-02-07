import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import csv

def remove_html(element):
        return element.string

r = requests.get('https://www.basketball-reference.com/players/a/')

if r.status_code >=200 and r.status_code <=299:
    soup = BeautifulSoup(r.text, 'html.parser')
    players_table = soup.select_one('#players')

    #CSS選擇器:https://www.w3schools.com/cssref/css_selectors.asp
    # 取得表頭
    headers = players_table.select('thead th')
    headers = list(map(remove_html, headers))

    # 取得內容
    contents = players_table.select('tbody tr:not(.thead)')

    result = [] 

    for content in contents:
        temp_list = []

        # player_name = content.select_one('th a').string
        # year_min = content.select('td')[0].string
        # year_max = content.select('td')[1].string
        # position = content.select('td')[2].string
        # height = content.select('td')[3].string
        # weight = content.select('td')[4].string
        # birth_date = content.select('td')[5].string
        # colleges = content.select('td')[6].string

        # temp_list.append(player_name)
        # temp_list.append(year_min)
        # temp_list.append(year_max)
        # temp_list.append(position)
        # temp_list.append(height)
        # temp_list.append(weight)
        # temp_list.append(birth_date)
        # temp_list.append(colleges)
        for i in range(7):
            temp_list.append(content.select('td')[i].string)
            pass
        
        result.append(temp_list)
        
        pass

    # print(result)

    with open("NBA球員資料.csv", "w",encoding='utf-8-sig') as file:
        csv_file = csv.writer(file)

        #表頭
        csv_file.writerow(headers)
        
        #內容
        for row in result:
            csv_file.writerow(row)
            pass