fresh_tea_list = [  {'name':'阿里山冰茶', 'price':"25",'尺寸':'L'},
                    {'name':'日月潭紅玉', 'price':"30",'尺寸':'L'},
                    {'name':'文山包種茶', 'price':"35",'尺寸':'XL'},

]


fresh_tea_list_price1 = int(fresh_tea_list[0]['price'])
fresh_tea_list_price2 = int(fresh_tea_list[1]['price'])
fresh_tea_list_price3 = int(fresh_tea_list[2]['price'])
total = fresh_tea_list_price1 + fresh_tea_list_price2 + fresh_tea_list_price3
print(total)

# fresh_tea_list_price=int(fresh_tea_list[0]['price'])+int(fresh_tea_list[1]['price'])+int(fresh_tea_list[2]['price'])
# print(fresh_tea_list_price)