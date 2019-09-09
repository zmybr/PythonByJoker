#email = 'qwe@163.com'
#for e in email :
 #   o=ord(e) - 10
 #   print(chr(o),end="")
#md5加密
#import hashlib
#md = hashlib.md5()#构造一个md5
#md.update('qwe@163.com'.encode())
#print(md.hexdigest())

#判断是否为闰年
#year = int(input('请输入年份'))
#if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#    print('是闰年')
#else:
#    print('不是闰年')

#1.温度转换
#C = float(input('请输入一个温度'))
#print((9/5)*C+32)
#2.圆柱体体积
#import math
#pai=math.pi
#radius = float(input("请输入半径"))
#length = float(input('请输入高'))
#area = radius * radius * pai
#volume = area * length
#print("The area is %.4f"%area)
#print("The volume is %.1f"%volume)
#3.英尺转换
#feet = float(input("请输入英尺"))
#meters = feet * 0.305
#print( "%f feet is %f meters"%(feet,meters))
#4.计算能量
#kg = float(input('Enter the amount of water in kilograms:'))
#init = float(input('Enter the initial temperature:'))
#final  = float(input('Enter the final temperature:'))
#Q = kg * (final - init) * 4184
#print("The energy needed is %.1f"%Q)
#5.计算利息
#balance = float(input('请输入差额：'))
#rate = float(input('请输入年利率：'))
#interest = balance * (rate / 1200)
#print('Th interest is %f'%interest)
#6.加速度
#v0,v1,t = eval(input('Enter v0,v1 and t:'))
#a = (v1 - v0)/t
#print('The average acceleration is %.4f'%a)
#7.复利值
#money = float(input("Enter the monthly saving amount:"))
#value = money * (1 + 0.00417)
#i=1
#while i < 6:
#    value = (money + value) * (1 + 0.00417)
#    i +=1
#print("After the sixth month,the account value is %.2f"%value)
#8.求和
num = int(input("Enter a number between 0 and 1000:"))
sum=0
b=num//100%10
c=num//10%10
a=num%10
sum=a+b+c
print('The sum of the digits is %d'%sum)
