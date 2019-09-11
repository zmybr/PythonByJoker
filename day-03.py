#五角数
# count = 0
# def getPentagonalNumber(n):
#     global count
#     for i in range(1,n+1):
#         s=(i*(3*i-1))/2
#         print('%d'%s,end="\t")
#         count += 1
#         if count % 10 == 0:
#             print()
# getPentagonalNumber(100)
#求和
# def sumDigits(n):
#     sum_=0
#     while n != 0:
#         a = n % 10
#         sum_ += a
#         b = n // 10
#         n = b
#     print(sum_)
# sumDigits(23)
#三个数排序
# def displaySortedNumbers(num1,num2,num3):
#     num=0
#     if num1>num2:
#         num=num2
#         num2=num1
#         num1=num
#     elif num1>num3:
#         num=num3
#         num3=num1
#         num1=num
#     elif num2>num3:
#         num=num3
#         num3=num2
#         num2=num
#     else:
#         print('%f=%f=%f'%(num1,num2,num3))
#     print(num1,num2,num3)
# num1,num2,num3 = eval(input('Enter three numbers: '))
# displaySortedNumbers(num1,num2,num3)
#计算投资
# def futurInvestmentValue(a,b,c):
#     month = a * (1 + b)
#     for i in range(0,c*12):
#         month = month * (1 + b)
#     print(month)
# futurInvestmentValue(10000,0.05/12,50)
#计算未来值
# def futur(invested,rate):
#     print('Years',end="\t")
#     print('Future Value')
#     for i in range(1,31):
#         month = invested * (1+(rate/100))
#         invested = month
#         print('%d'%i,end='\t')
#         print('%.2f'%month)
# invested = float(input('The amount invested: '))
# rate = int(input('Annual interest rate: '))
# futur(invested,rate)
#显示字符
# def printChars(ch1,ch2,numberPerLine):
#     count = 0
#     a=ord(ch1)
#     b=ord(ch2)
#     for i in range(a-1,b):
#         if 48<= a <= 57:
#             print(chr(int(ch1)+i),end=" ")
#         elif 65<= a <= 90:
#             print(chr(int(ch1)+i),end=" ")
#         elif 97<= a <=122:
#             print(chr(int(ch1)+i),end=" ")
#         count += 1
#         if count % numberPerLine == 0:
#             print(" ")
# ch1 = input('请输入第一个字符')
# ch2 = input('请输入最后一个字符')
# numberPerLine = int(input('每行打印几个：'))   
# printChars(ch1,ch2,numberPerLine)
#年天数
# def numberOfDaysInAYear(year1,yera2):
#     for i in range(year1,yera2+1):
#         if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
#             print("%d是闰年，天数为366天"%i)
#         else:
#             print("%d是平年，天数为365天"%i)
# numberOfDaysInAYear(2010,2020)
#距离
# import math
# sqrt=math.sqrt
# def distance(x1,y1,x2,y2):
#     a=sqrt((x1-x2)**2+(y1-y2)**2)
#     print(a)
# x1,x2 = eval(input('请输入第一个点的坐标： '))
# y1,y2 = eval(input('请输入第二个点的坐标： '))
# distance(x1,x2,y1,y2)
#梅森素数--------------------------------------------------------------------------------------------------
# def meisensushu(num):
#     for i in range(2,num):
#         for j in range(2,i):
#             if i % j == 0:  
#                 break
#         else:
#             print(i)
#         if 2**(i-1)==i:
#             print(i)
# meisensushu(31)
#---------------------------------------------------------------------------------------------------------
#时间日期
# import time
# def times():
#     print ("Current date and time is %s"%time.asctime(time.localtime(time.time())))
# times()
#投骰子----------------------------------------------------------------------------------------------------
# import random
# ds=random.randint(1,6)
# ds1=random.randint(1,6)
# def touzi():
#     if ds+ds1==2 or ds+ds1==3 or ds+ds1==12:
#         print(ds+ds1)
#         print('You lose')
#     elif ds+ds1==7 or ds+ds1==11:
#         print(ds+ds1)
#         print('You win')
#     else:
#         a=ds+ds1
#         if ds+ds1 == 7:
#             print(ds+ds1)
#             print('You win')
#         elif ds+ds1==a :
#             print(ds+ds1)
#             print('You lose')       
# touzi()
#----------------------------------------------------------------------------------------------------------
