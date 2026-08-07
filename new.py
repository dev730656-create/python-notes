# # # # # # # # # # def add(a,b):
# # # # # # # # # #     return a+b
# # # # # # # # # # result=add(1,2)
# # # # # # # # # # print(result)
# # # # # # # # # # def add(a,b):
# # # # # # # # # #     print(a+b)
# # # # # # # # # # result=add(1,2)
# # # # # # # # # # print(result)
# # # # # # # # def welcome():
# # # # # # # #      print("welcome")
# # # # # # # # welcome()
# # # # # # # # welcome()
# # # # # # # # welcome()
# # # # # # # # def greet():
# # # # # # # #     print("hello")
# # # # # # # print("a")
# # # # # # # def greet():
# # # # # # #     print("hello")
# # # # # # #     print("b")
# # # # # # # greet()
# # # # # # def test():
# # # # # #     print("a")
# # # # # #     return
# # # # # #     print("b")
# # # # # # test()
# # # # # def stats(a,b):
# # # # #     return a+b,a*b
# # # # # s,p=stats(2,4)
# # # # # print("sum",s)
# # # # # print("product",p)
# # # # square=lambda x:x*x
# # # # print(square(5))
# # # add=lambda a,b:a+b
# # # print(add(10,20))
# # def greet(name,age):
# #     print("name",name)
# #     print("age",age)
# # greet("achu",20)
# def greet(name,age):
#  print("name",name)
#  print("age",age)
# greet(age=20,name="hello")
def total(numbers):
    result = 0
    for n in numbers:
        result += n
    return result



