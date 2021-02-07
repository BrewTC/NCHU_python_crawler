import json

article = {}
article['post_number'] = "爆"
article['title'] = "Re: [新聞] 特斯拉是今年最大贏家 電動車概念股"

article1 = {}
article1['post_number'] = "99"
article1['title'] = "[請益] 35歲擁有750萬現金可以全職炒股"

article2 = {}
article2['post_number'] = "51"
article2['title'] = "Re: [請益] 股票玩到走火入魔"

article_list = []
article_list.append(article)
article_list.append(article1)
article_list.append(article2)
print(article_list)

article_json = json.dumps(article_list, ensure_ascii=False) #中文字會不見，所以加上後面
#print(article_json)

with open('123.txt ','wt', encoding='UTF-8') as file:
    for line in file:
        file.write(article_json)
