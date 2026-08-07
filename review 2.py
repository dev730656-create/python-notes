#tuple
"""ordered
duplicates
collection of elements writen inside()
used to store fixed data
scenario=days of a week
"""
num=(1,2,3,4)
# print(num[2])#index
print(num.count(4))#count


#dictionary
"""ordered
duplicates
mutable
collection of elements writen inside{} as key value pairs
scenario=student details

"""
# student_details={"name":"deva","age":20,"mark":50,"grade":"b"}
# print(student_details.keys())#return all keys

# print(student_details.values())#return all values

# print(student_details.items())#return all key-value pair

# student_details.update({"age":30})#update value
# print(student_details)

# print(student_details.pop("name"))#removes a key and return a value

# student_details.popitem()#it removes the last inserted key value pair
# print(student_details)

# print(student_details)#remove all the key vale pairs

# student_details.copy()#make a copy of this same dictionary
# print(student_details)


# keys=["id","age","mark","grade"]#create new dictionary using same keys
# new_dic= dict.fromkeys(keys,1)
# print(new_dic)

#set
"""
unorderd
mutable
no duplication
collection of unique elements
scenario=attendence
"""

# s={1,2,3}
# p={7,8,9}
# s.add(4)
# print(s)

# s.update([5,6,7,8])
# print(s)

# s.remove(1)
# print(s)

# # s.clear()
# # print(s)

# s.discard(10)
# print(s)

# s.copy()
# print(s)

# print(s.union)

x={3}
b={4,5,3}
print(x.intersection(b))
print(x.union(b))
print(x.difference(b))
print(x.symmetric_difference(b))

print(x.issubset(b))
print(b.issuperset(x))

print(x.isdisjoint(b))










