# 串列的操作

# 1. 建立空的串列
x_list = []
y_list = list()
z_list = [55, 66, 77, 88] #建立並附值
print(z_list)
# 2. 新增值進去串列
print(z_list.append(78))
# 3. 取出數值
print(z_list[2])
# 4. 刪除數值
print(z_list.pop(-1)) #刪除並會回傳
del z_list[1] #以索引值刪除
print(z_list)
z_list.remove(55) #以內容方式刪除(只會刪除一次)
# 5. 排序
z_list.sort() #從小排到大
z_list.sort(reverse=True) #從大排到小

z_list.reverse()#順序顛倒
# 6. 其他
len(z_list) #算長度
max(z_list) #最大值
min(z_list) #最小值
sum(z_list) #總和