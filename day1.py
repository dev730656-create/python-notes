"""module1"""# print("hello world")
2# a=10
# b=20
# add=a+b
# print(add)
#  """another way(if the value defined by user)"""
# num1=int(input("enter your first number"))
# num2=int(input("enter your second number"))
# result=num1+num2
# print(result)
3# name=input("enter your name")
# print("your name is:",name)
# age=int(input("enter your age"))
# print("your age is",age)
3# age=10
# print(type(age))
# a=5
# print(isinstance(a,float))
# print(isinstance(a,int))
# a=5
# b=a
# print(id(a))
# print(id(b))
# a=10
# b=20
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# age = 16
# elligible_licence = False
# if age<=18 or elligible_licence:
#     print("allowed")
#     marks=50
#     if marks>=90:
#         print("a grade")
#     if marks>=70:
#         print("b grade")
#     if marks>=50:
#         print("c grade")
#
# num=int(input("enter your number"))
# for i in range(1,10):
#     print(num*i)
# i=1
# while i<=5:
#     print(i)
#     i=i+1
# for i in range(1,10):
#     if i==5:
#         pass
#     print(i)

# def greet(name):
#     print("hello",name)
# greet("deva")
# name=input("enter your name")
# age=int(input("enter your number"))
# def greet(name,age):
#     print("hey",name)
#     print("hello",age)
# greet(name,age)
# def greet(name="guest"):
#     print("hello",name)
# greet()
# greet("deva")
def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)
num=int(input("enter your number"))
print(factorial(num))

    


        










