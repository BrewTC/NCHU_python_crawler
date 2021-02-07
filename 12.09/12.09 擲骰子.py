'''
#(n1,n2,n3)=(6,6,6)
import random
number1 = random.randint(1,6)
number2 = random.randint(1,6)
number3 = random.randint(1,6)
count = 1
# != 是不等於的意思
while number1 !=6 or number2 !=6 or number3 !=6:
    print(number1,number2,number3) #骰錯就在繼續亂數骰
    number1 = random.randint(1,6)
    number2 = random.randint(1,6)
    number3 = random.randint(1,6)
    count += 1

print(number1,number2,number3)
print("總計骰了:",count,"次")
'''

'''
#我的解法
#n1+n2+n3=18(總數會是18)
number = 18
import random
n1 = random.randint(3,18)
c = 1
while n1 != 18:
    print(n1)
    n1 = random.randint(3,18)
    c += 1

print(n1)
print("總共骰了:",c,"次")
'''

#另一種解法
#當三個骰子加總不為18的時候，要重新擲骰子
import random
number1 = random.randint(1,6)
number2 = random.randint(1,6)
number3 = random.randint(1,6)
count = 1
while number1+number2+number3 !=18:
    print(number1,number2,number3)
    number1 = random.randint(1,6)
    number2 = random.randint(1,6)
    number3 = random.randint(1,6)
    count += 1 #count = count+1

print(number1,number2,number3)
print('擲骰子次數:', count)