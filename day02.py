#1.几何学:五边形面积
# import math
# sin = math.sin
# tan = math.tan
# pai = math.pi
# r = float(input('请输入半径:'))
# s = 2 * r * (sin (pai / 5))
# area = 5 * s * s / (4 * tan (pai / 5))
# print('The area of the pentagon is %.2f'%area)
#2.几何学：大圆距离
# import math
# sin=math.sin
# cos=math.cos
# arccos=math.acos
# radins=math.radians
# x1,y1 = eval(input('Enter point 1:'))
# x2,y2 = eval(input('Enter point 2:'))
# x1=radins(x1)
# x2=radins(x2)
# y1=radins(y1)
# y2=radins(y2)
# d = 6371.01 *arccos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1-y2))
# print(d)
#3.几何学：五角形面积
# import math
# tan=math.tan
# pai=math.pi
# s = float(input('Enter the side:'))
# Area = (5 * s * s)/(4*tan(pai/5))
# print("The area of the pentagon is %f"%Area)
#4.几何学：一个正多边形的面积
# import math
# tan=math.tan
# pai=math.pi
# n = int(input('Enter the number of sides:'))
# s = float(input('Enter the side:'))
# Area = (n * s * s)/(4 * tan(pai/n))
# print('The area of the polygon is %f'%Area)
#5.找出ASCII码的字符
# num = int(input('Enter an ASCII code:'))
# print(chr(num))
#6.工资表
# name = str(input('Enter employee is name:'))
# time = int(input('Enter number of hours worked in a week:'))
# pay = float(input('Enter hourly pay rate:'))
# tax1 = float(input('Enter federal tax withholding rate:'))
# tax2 = float(input('Enter state tax withholding rate:'))
# print()
# print('Employee Name:%s'%name)
# print('Hours Worked:%d'%time)
# print('Pay Rate:$%.2f'%pay)
# print('Gross Pay:$%.2f'%(pay * time))
# print('Deductions:')
# print('  Federal Withholding(%.2f):%.2f'%(tax1,(pay * time * tax1)))
# print('  State Withholding(%.2f):%.2f'%(tax2,(pay * time * tax2)))
# print('  Total Deduction:%.2f'%((pay * time * tax1)+(pay * time * tax2)))
# print('Net Pay:$%.2f'%((pay * time)-((pay * time * tax1)+(pay * time * tax2))))
#7.反向数字
# num = str(input('Enter an integer:'))
# num1 = num[::-1]
# print(num1)
#1.解一元二次方程
# import math
# gen = math.sqrt
# a,b,c = eval(input('Enter a,b,c:'))
# x = (b*b)-(4*a*c)
# if x>0:
#     r1=(-b + gen(x))/(2*a)
#     r2=(-b - gen(x))/(2*a)
#     print("The roots are %fand %f"%(r1,r2))
# elif  x==0:
#     r=(-b)/(2*a)
#     print('The root is%f'%r)
# else:
#     print('The equation has no real roots')
# 2.学习加法
# import random
# num1 = random.randint(0,100)
# num2 = random.randint(0,100)
# print(num1,num2)
# he = int(input('请输入结果：'))
# _sum=num1+num2
# if _sum == he:
#     print('结果为真')
# else:
#     print('结果为假')
# print('结果为：%d'%_sum)
#3.找未来数据
# today = int(input('Enter today is day:'))
# day = int(input('Enter the number of days elapsed since today:'))
# if today==0:
#     b='sunday'
# elif today==1:
#     b='monday'
# elif today==2:
#     b='tuesday'
# elif today==3:
#     b='wednesday'
# elif today==4:
#     b='thursday'
# elif today==5:
#     b='friday'
# elif today==6:
#     b='saturday'
# days = day % 7
# todays=today+days
# if todays==0:
#     a='sunday'
# elif todays==1:
#     a='monday'
# elif todays==2:
#     a='tuesday'
# elif todays==3:
#     a='wednesday'
# elif todays==4:
#     a='thursday'
# elif todays==5:
#     a='friday'
# elif todays==6:
#     a='saturday'
# print("Today is %s and the future day is %s"%(b,a))
#4.排序
# a = input('请输入第1个数:')
# b = input('请输入第2个数:')
# c = input('请输入第3个数:')
# d=0
# if a>b:
#    d=a
#    a=b
#    b=d
# elif a>c:
#     d=a
#     a=c
#     c=d
# elif b>c:
#     d=b
#     b=c
#     c=d
# else:
#     print("a=b=c")
# print(a,b,c)
#5.价钱比较
# weight1,price1 = eval(input('Enter weight and price for package 1:'))
# weight2,price2 = eval(input('Enter weight and price for package 2:'))
# price = weight1/price1
# price0 = weight2/price2
# if price>price0:
#     print('Package 1 has the better price.')
# else:
#     print('Package 2 has the better price.')
#6.找出一个月中的天数
# year = int(input('请输入年份：'))
# mouth = int(input('请输入月份(1-12)：'))
# if mouth==1 or mouth==3 or mouth==5 or mouth==7 or mouth==8 or mouth==10 or mouth==12:
#     print('%d年%d月有31天'%(year,mouth))
# elif mouth==4 or mouth==6 or mouth==9 or mouth==11:
#     print('%d年%d月有30天'%(year,mouth))
# elif mouth==2 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print('%d年%d月有29天'%(year,mouth))
# else:
#     print('%d年%d月有28天'%(year,mouth))
#7.头或尾
# import random
# num1 = random.randint(0,1)
# user = int(input('请输入0或1（0为正面，1为反面）:'))
# if num1==user:
#     print('猜测正确')
# else:
#     print('猜测错误')
# print('系统为:%d'%num1)
#8.石头，剪刀，布
# import random
# computer = random.randint(0,2)
# player= int(input("请输入0,1,2(0代表剪刀，1代表石头，2代表布)："))
# if computer==0:
#     print('scissor')
# elif computer==1:
#     print('rock')
# else:
#     print('paper')
# if player==computer:
#     print("平局")
# elif player==0 and computer==2:
#     print('你赢了')
# elif player==1 and computer==0:
#     print('你赢了')
# elif player==2 and computer==1:
#     print('你赢了')
# else:
#     print('你输了') 
# 9.一周的星期几
year = int(input('Enter year:'))
month = int(input('Enter month:1-12:'))
day = int(input('Enter the day of the month:1-31:'))
j = year/100
k = year%100
if month == 1:
    h = ((day+((26*14)/10)//1+(year-1)%100+(((year-1)%100)/4)//1+(((year-1)/100)/4)//1+5*j)%7)
    x = h
if month == 2:
    h = ((day+((26*15)/10)//1+(year-1)%100+(((year-1)%100)/4)//1+(((year-1)/100)/4)//1+5*j)%7)
    x = h
else:
     h = int((day+(26*(month+1)/10)//1+k+(k/4)//1 + (j/4)//1+5*j)%7)
     x = h
if x == 0:
    print('星期六')
elif x == 1:
    print('星期天')
elif x == 2:
    print('星期一')
elif x == 3:
    print('星期二')
elif x == 4:
    print('星期三')
elif x == 5:
    print('星期四')
elif x == 6:
    print('星期五')
else:
    print('error')

#10.选牌
# import numpy as np
# num= np.random.choice(['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'])
# num1= np.random.choice(['梅花','红桃','方块','黑桃'])
# print('The card you picked is the %s of %s'%(num,num1))
#11回文数
# num = str(input("Enter a three-digit integer:"))
# num1=num[::-1]
# if num==num1:
#     print('%s is a pailindrome'%num)
# else:
#     print('%s is not a pailindrome'%num)
#12.三角形周长
# a,b,c = eval(input('Enter three edges:'))
# if a+b>c and a+c>b and b+c>a:
#     print('The perimeter is %d'%(a+b+c))
# else:
#     print('输入非法')
#1.平均值
# num=1
# a=0
# b=0
# _sum=0
# while num != 0:
#     num = int(input("Enter an integer,the input ends if it is 0:"))
#     if num>0 :
#         a +=1
#     elif num<0:
#         b +=1
#     _sum +=num
# pj=_sum/(a+b)
# print('正数有：%d,负数有:%d,平均值为:%.2f'%(a,b,pj))
#2.计算未来学费
# value = 10000 * (1 + 0.05)
# i=1
# value1=0
# while i < 10:
#    value = value* (1 + 0.05)
#    if i<4:
#     value1 = value1+value
#    i +=1
# print("After the ten year,the account value is %.2f"%value)
# print("After the four year,all value is %.2f"%value1)
#4.整除
# count=0
# for i in range(100,1001):
#     if i%5==0 and i%6==0:
#         count +=1
#         print(i,end=" ")   
#         if count % 10 == 0:
#             print("")
#5
# n=0
# num=0
# while n<12000:
#     num +=1
#     n=num*num
# else:
#     print(num)
# n=0
# num=0
# while n < 12000:
#     num += 1
#     n = num*num*num
# else:
#     print(num-1)
#7.演示消除错误
# _sum=0
# _sum1=0
# for i in range(1,50000):
#     _sum +=1/i
# print(_sum)
# for i in range(50000,0,-1):
#     _sum1 +=1/i
# print(_sum1)
#8.数列求和
# _sum=0
# for i in range(3,100,2):
#     _sum +=(i-2)/i
# print(_sum)
#9.计算Π
# i = int(input("请输入i值:"))
# pai=0
# for i in range(i):
#     pai=pai+(((-1)**(i+1))/(2*i-1))
# s=pai*4
# print(s)
#10.完全数
# for i in range(1,10000):
#     s=0
#     for j in range(1,i):
#         if i%j==0:
#             s=s+j
#     if i==s:
#         print(i)
#11.组合
# count = 0
# for i in range(1,8):
#     for j in range(1,i):
#         print(j,i)
#         count +=1
# print('The total number of all combinations is %d'%count)
