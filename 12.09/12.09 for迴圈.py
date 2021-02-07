# for x in range(10):
#     print("Hello, line{}".format(x))
# for z in range(1,11):
#     print(z) #[0,1,2,3,4,5,6,7,8,9,10]

# x = list(range(10))
# print(x)



# x_list = [12,31,53,71,99,22,11,44]
# odd_count = 0
# even_count = 0

# for i in x_list:
#     if i%2 == 1:
#         odd_count += 1
#     else:
#         even_count += 1
#     print("奇數:",odd_count,"偶數:",even_count)



#題目: [80,39,22,59,30,100,67,81]
grade = input("請輸入成績，並使用逗號分隔開來:")
grade_list = grade.split(",")
grade_list_1 = list(map(int,grade_list))

#最精簡寫法 score = list(map(int,input("請輸入成績，並使用逗號分隔開來:").split(',')))

pass_list = []
fail_list = []

for i in grade_list_1:
    if i>=60:
        pass_list.append(i)
    else:
        fail_list.append(i)
print("及格的人數:", len(pass_list), "不及格的人數:", len(fail_list))
print("最高分數", max(pass_list))
print("最低分數", min(fail_list))