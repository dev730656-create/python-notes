# 1.num=int(input("enter your number"))
# if num%2==0:
#     print("number is even")
# else:
#         print("number is odd")
# 2.num=int(input("enter your number"))
# if num>0:
#     print("number is +ve")
# elif num<0:
#     print("number is _ve")
# elif num==0:
#     print("number is zero")
# else:
#     print("number is invalid")
# 3.num1=int(input("enter your first number"))
# num2=int(input("enter your second number"))
# if num1>num2:
#     print("num1 is greter")
# else:
#     print("num2 is greter")
# 4.num1=int(input("enter your first number"))
# num2=int(input("enter your second number"))
# num3=int(input("enter your third number"))
# if num1>num2:
#      print("number1 is greater")
# elif num2>num3:
#      print("number2 is greater")
# elif num3>num1:
#      print("number3 is greater")
# else:
#      print("number is invalid")
# 5.
# age=int(input("enter your age"))
# if age>=18:
#     print("you are eligible")
# else:
#     print("you are not eligible")
# 6.
# for i in range(1,11):
#     print(i)
7.
# for i in range(2,21,2):
#     print(i)
8.
# num=int(input("enter your number"))
# sum=0
# for i in range(1,num+1):
#     sum=sum+i
# print(sum)
9.
# num=int(input("enter your number"))
# total=0
# for i in range(1,13):
#     total=num*num-1
#     print(num,"*",i,"=",num*i)
# 10.count=1
# while count<10:
#      print(count)
#      count=count+1
#11.for i in range(10,0,-1):
#     print(i)
12.
# sum = 0
# while True:
#     num = int(input("Enter a number: "))
#     if num == 0:
#         break
#     sum = sum + num
# print("Total is", sum)
# 13.
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i)
# 14.
# for i in range(1, 11):
#     if i == 7:
#         break
#     print(i)
# 15.
# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)
# 16.
# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i
# print("Factorial is", fact)
# 17.
# num = int(input("Enter a number: "))
# count = 0
# while num > 0:
#     num = num // 10
#     count = count + 1

# print("Number of digits =", count)
# 18.
# num = int(input("Enter a number: "))
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print("Reverse =", reverse)
# 19.
# num = int(input("Enter a number: "))
# original = num
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
20.
password = "python123"
user_password = input("Enter the password: ")
if user_password == password:
    print("Access Granted")
else:
    print("Wrong Password")













