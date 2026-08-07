# word="python"
# print(word[-4])

# text="hello"
# print(text[::])
# print(text[::-1])
# print(text[::2])

# word="hello"
# word[0]="j"

# f="hello"
# s="world"
# print(f+" "+s)
# msg="good" 
# msg+="morning"
# print(msg)

# words=["python","is","awesome"]
# print(",".join(words))
# name="veena"
# age=30
# print(f"{name} is {age} years old")
# age=25
# print(f"age {age}")
# mixed=[10,"python",3.5,True]
# print(mixed)
# numbers[3]=20
# print(numbers)
# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[::-1])
# numbers=[1,2,3]
# numbers.append(4,5)
# numbers[0]=10
# print(numbers)
# nums=[1,2]
# print(nums.extend(4,5,6))
# nums=[10,20,30]
# x=nums.pop()
# print(x)
# num=[1,2,3]
# print(num.clear())
# nums=[10,20,30,40]
# print(nums.index(20))
# nums=[1,2,3,2,4,2,2]
# print(nums.count(2))
# nums=[6,7,2,4]
# sorted(nums)
# print(nums)
# nums=[3,2,1]
# num_list=sorted(nums)
# print(nums)
# print(num_list)
# n
# fruits=["a","b","c"]
# for fruit in range(len(fruits)):
#     print(fruits[fruit])
# nums=[1,2,3]
# n=2 in nums
# print(n)
# print(7 not in nums)

# a=[1,2,3]
# # b=[2,4,5,6]
# print(a*2)

# a=[[1,2,3],[3,4]]
# print(a[0])
# print(a[1])
# print(a[0][2])
# print(a[1][0])

# numbers=(1,2)
# print(type(numbers))

# numbers=()
# print(type(numbers))

# numbers=(5)
# print(type(numbers))

# a=10,20#why because of ","//tuple packing
# print(type(a))

# point=(10,20)
# x,y=point
# print(x,y)

# colors=("red","blue")
# print(colors[0])

# numbers=[1,2,3,4,5]
# # print(numbers[1:4])
# print(numbers[::-1])#?

# colors=("red","blue")
# colors[0]="yellow"
# print(colors)

nums=[1,2,3,4,4]
print(nums.count(4))

nums=[1,2,3,4]
print(nums.index(4))


# colors=("red","blue")
# for i in colors:
#     print(colors)

# student=("achu",20)#?
# name=student[0]
# age=student[1]
# print(name)
# print(age)
# name,age=student
# print(student)

# numbers=(1,2,3,4,5)#collect the remaining values//extended unpacking
# a,b,*c=numbers
# print("a=",a)
# print("b=",b)
# print("c=",c)

nums_list=[1,2,3]
nums_tuple=tuple(nums_list)
nums_list=list(nums_tuple)

data=((1,2)(3,4))
print(data[1][0])
print(data[0][1])
print(data[1][1])
print(data)


































