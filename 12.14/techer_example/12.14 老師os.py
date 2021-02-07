import os


directory_name = "1214_data"

# 是否有這個資料夾存在，如果不存在 就建立一個新的資料夾
if not directory_name in os.listdir(): #true or false
    os.mkdir(directory_name)

#wt新增/會一直覆蓋掉舊的 ，a附加舊的資料上去
#fp = open("1214_data/mydata.txt", "a")
fp = open(directory_name+"/mydata.txt", "a")
#fp = open("{}/mydata.txt".format(directory_name), "a")

fp.write("This is my data!\n")
fp.write("This is my data!\n")
fp.write("This is my data!")
fp.close() #很重要，要寫