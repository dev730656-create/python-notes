
# x=20
# def show():
#      global x
#      x=10
#      print(x)
# show()
# print(x)
# def outer():
#     x="outer"
#     def inner():
#         nonlocal x
#         x="inner" 
#     inner()
#     print("x after inner()",x)
# outer()
# x="global"
# def outer():
#     x="enclosing"
#     def inner():
#         x="local"
#         print("inner x:",x)
#     inner()
#     print("outer x:",x)
# outer()
# print("global keyword:",x)
def countdown(n):
    print(n)
    if n>1:
        countdown(n-1)
countdown(5)


