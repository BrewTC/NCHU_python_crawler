x = input("輸入學生成績，並以逗點方式間格:") #輸入的資料為字串
print(x)
x_list = x.split(",")
#將input的str用,分割
x_number_list = list(map(int,x_list))
#新設一個list 用map函式轉換為int的list
print(x_number_list)

total = sum(x_number_list)
print("總分為: ", total)
svg = sum(x_number_list)/len(x_number_list)
print("平均為: ", svg)


# score1, score2, score3 = map(int.input("請輸入成績:"))
# list_score = []
# list_score.append(score1)
# list_score.append(score2)
# list_score.append(score3)
# print(list_score)
# total = sum(list_score)
# print(total)

test_string = "小火慢炒到香氣逼人的熟花生，裹上甜度適中的濃郁巧克力，讓人忍不住想一口接一口。這款焙香花生巧克力，免烤箱做法簡單又快速，連小學生都可以完美勝任，有親朋好友來家中作客時，端出一盤，再沏壺熱茶款待，或是當成伴手禮送出，都很合適～"

test_list = list(test_string)
print(test_list)

test_join = " ".join(test_list)
print(test_join)