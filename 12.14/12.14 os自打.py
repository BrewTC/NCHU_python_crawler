#https://nkust.gitbook.io/python/an-cao-zuo-fang-fa
import os

#print(os.listdir()) #印出目前所在檔案位置 C:\Users\Surface\Desktop\109>

directory_name = "1214_data"
#在目錄下新增"data"資料夾
os.mkdir("directory_name")

#是否有這個資料夾存在，接著再做後續的動作
if not directory_name in os.listdir(): #true or flase
    os.mkdir(directory_name)
#存在這個資料夾

#fp = open("1214_data/mydata/mydata.txt","a")
fp = open(directory_name + "/mydata.txt","a")
#fp = open(("{}/mydata.txt".format(directory_name),"a"))

#wt新增會一直覆蓋掉舊的，a附加舊的資料上去
fp = open("mydata.txt", "w")
fp.write("This is my data!\n")
fp.write("This is my data!\n")
fp.write("This is my data!")
fp.close()