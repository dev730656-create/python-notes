"""type of function"""
# def area(a):#function definition
#     print(a*a)#function call
# area(5)
# square=lambda a:a*a#using lambda function
# print(square(2))
# def add(a,b):#using return statement
#     return a+b
# print(add(10,20))
# print(add(10,20,30))
# def greet(a):
#     print("hello")#function definition and function call
#     print(a+a)
# greet(20)/
# print("a")
# def greet():
#     return 
# def hello():
#     print("hello")
# hello()
# def calc(a,b,c):
#     return a+b,a-b,a*b #multiple values returning case
# c,p,d=calc(10,2,4)
# print(d)
# def greet(name,age):#positional arguments
#      print("name:",name)
#      print("age:",age)
# greet(20,"deva")
# def greet(name,age):#keyword arguments
#      print("name:",name)
#      print("age:",age)
# greet(age=20,name="deva")

# def greet(name="guest"):
#      print("welome",name)
# greet()

# def greet(age,name="guest"):
#       print(age,name)
# greet(10)

# def add(*numbers):
#       print(numbers)
# add(10,20,30)

# def student(**details):
#       print(details)
# student(age=20,name="anu",student_id=10,classes=6)

# x=10
# def greet():
#     print(x)
# greet()

# def greet():
#     x=10
#     print(x)
# greet()

# x=10
# def greet():
#     global x
#     x=20 
# greet()  
# print(x)


# def outside():
#     x=10
#     def inside():
#         nonlocal x
#     x=20
#     inside()
#     print(x)
# outside()
# n=int(input("enter you number"))
# def factorial(n):
#     if n==1:
#      return 1
#     return n*factorial(n-1)
# print(factorial(n))

def count(n):
   print(n)
   if n>1:
     count(n-1)
     print(count(6))



    


















