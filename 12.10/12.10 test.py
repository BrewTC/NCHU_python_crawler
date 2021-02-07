'''
#自己的寫法
x = input("請輸入5個正整數，並用逗號分隔開來:")
x_list = x.split(",")
x_list1 = list(map(int,x_list)) #可以不需要用map在轉換為int狀態
print(x_list1)

for i in x_list1:
    del x_list1[0]
    x_list1.sort()
    print(x_list1)
    del x_list1[0]
    x_list1.sort(reverse=True)
    print(x_list1)
'''


'''
5
99 77 66 44 11
7
1 98 95 52 56 34 43
'''

#老師的解法
number_len = int(input())
number_string = input()
#print(number_string)
#99 77 66 44 11 str
number_list = number_string.split()
#["99","77","66","44","11"]
for i in range(number_len-1):
    number_list.reverse()     #reverse(),將list做反向的排序
    number_list.pop()
    print(number_list)
    pass