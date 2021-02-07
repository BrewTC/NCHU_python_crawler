# x = int(input("請輸入一個正整數: "))

# if x%2 ==1:
#     print("這個數字為奇數")
#     pass
# else:
#     print("這個數字為偶數")
#     pass

#請輸入三個數字判斷是否可以形成三角形

x = input("請輸入三個正整數，並以逗點方式間格:")
x_list = list(x.split(','))
x_list.sort(reverse=True)
x_list_small = x_list[1]+x_list[2]

if x_list[0] > x_list_small:
    print("可以形成三角形!")
else:
    print("不可以形成三角形!")