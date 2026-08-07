# def greet():
#     print("welcome")
# greet()
# greet()
# greet()
# def greet(name):
#     print("name is:",name)
# greet("arya")
# def add(a,b):
#     return a+b
# print(add(10,20))
# x=10
# square=lambda x:x*x
# print(square(5))

# def square(x):
#     return x*x
# print(square(5))


# def add(a,b):
#     return a+b
# sum=add(10,40)
# print(sum)

# def add(a,b):
#     print(a+b)
# add(10,200)

# def greet(name="guest"):
#     print("welcome",name)
# greet("rudra")

# def total(*numbers):
#     sum=0
#     for i in numbers:
#       sum=sum+i
#     return sum
# print(total(10,20,30))

# def student(**details):
#    return details
# print(student(name="laya",age=10,mark=50))

# x=10
# def greet():
#     global x
#     x=20
#     print(x)
# greet()
# def countdown(n):
#    if n==0:
#     return n
#    print(n)
#    countdown(n-1)
# countdown(5)

# def factorial(n):
#   if n==1:
#         return 1
#   return n*factorial(n-1)
# print(factorial(7))


# def total(*numbers):
#     sum=0
#     for i in numbers:
#      sum=sum+i
#     return sum
#     sum=sum+numbers
# print(total(1,4))

# def greet(age,value):
#    print("age is",value)
#    print("value is",age)
# greet(1,2)

# def countdown(n):
#    if n==0:
#       return n
#    print(n)
#    countdown(n-1)
# countdown(5)

# def factorial(n):
#    if n==1:
#       return 1
#    return n*factorial(n-1)
# print(factorial(6))

# #control statements

# for i in range(1,11):
#    print(i):

num=int(input("enter your number"))
for i in range(1,11):
    print(i,"x",num,"=",num*i)

