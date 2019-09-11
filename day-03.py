#1.函数，奇偶数
# def zm(num):
#     if num%2==0:
#         print("偶数 %d"%num)
#     else:
#         print('奇数 %d'%num)
# zm(2)
# zm(5)
#2.函数，素数
# def ybr(num):
#     for i in range(2,num):
#         if num % i == 0:  
#             print('%d不是素数'%num) 
#             break
#     else:
#         print('%d是素数'%num)
# ybr(9)
# ybr(11)
#3.函数，验证码
# import random
# def zybrm() :
#     yzm = random.randrange(1000,9999)
#     #res = int(input('验证码是：%d,请输入：'%yzm))
#     print(yzm)
#     res = int(input('请输入验证码：'))
#     if res == yzm :
#         print('验证码正确')
#     else :
#         print('验证码错误')
# zybrm()
# import numpy as np
# def yzbmr():
#     for i in range(4):
#         yzm = np.random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
#         print(yzm,end="")
# yzbmr()
#4.函数，登陆0
# count = 1
# import random
# def zmybr():
#     global count
#     username = input('请输入账号：')
#     password = input('请输入密码：')
#     yzm = random.randrange(1000,9999)
#     res = int(input('验证码是：%d,请输入：'%yzm))
#     if yzm == res :
#         if username=='abc':
#             if password=='123' :
#                 print('登陆成功')
#             else:
#                 print('登陆失败')
#         else:
#             print('用户名错误')
#             if count != 3:
#                 count +=1
#                 zmybr()
#             else:
#                 print('尝试次数达到上限')
#     else:
#         print('验证码错误')
# zmybr()
#5.函数，登陆1
# import numpy as np
# ORIGINAL_USERNAME = 'admin'
# ORIGINAL_PASSWORD = '123'
# LOGINCOUNT=1
# def Check(username, password):
#     # 当函数体内需要改变外部变量的时候我们才需要global,但是统一起见都写上
#     global ORIGINAL_USERNAME, ORIGINAL_PASSWORD,LOGINCOUNT
#     if username == ORIGINAL_USERNAME and password == ORIGINAL_PASSWORD:
#         print('登录成功')
#     else:
#         print('登录失败')
#         if LOGINCOUNT != 3:
#             LOGINCOUNT +=1
#             Login()
#         else:
#             print('尝试次数达到上限')
        
# def Login():
#     username = input('请输入账号:>>')
#     password = input('请输入密码:>>')
#     V_res = Verify()
#     if V_res == True:
#         Check(username, password)
#     else:
#         for _ in range(4):
#             V_res = Verify()
#             if V_res:
#                 Check(username, password)
#                 break
#         else:
#             print('验证码错误次数过多,怀疑你是一个机器人.')

# def Verify():
#     """
#     生成验证码
#     """
#     word = ""
#     word_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r',
#                 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k',
#                 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
#     for _ in range(4):
#         word += np.random.choice(word_list)
#     user_word = input('请输入验证码%s:>>'%word)
#     if user_word == word:
#         return True
#     else:
#         return False

# def API():
#     pass

# def Start():
#     Login()

# if __name__ == "__main__":
#     Start()
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
#投骰子
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