# 1.define a variable
# x = 1
# print(int(x), type(int(x)))
# print(float(x), type(float(x)))
# print(str(x), type(str(x)))
from dataclasses import replace

import append

# x = 1
# y = 2.0
# z = "123"
# print(x, type(x))
# print(y,type(y))
# print(z,type(z))

# 2.Redeclare the value
# x = 2
# print(int(x), type(int(x)))
# print(float(x), type(float(x)))
# print(str(x), type(str(x)))

# 3.Assigning a single value
# x = 10
# a = x
# b = x
# c = x
# print(a==b==c, x)
# print(x)

# 4.Assign two variables a and b as integer and print the sum of a+b

# a = 3
# b = 5
# result = a + b
# print("value of a is" , a)
# print("value of b is" , b)
# print("Sum of a+b is", result, type(result))

# 5.Write a Python program to create a list with five different fruits. eg:fruits = ["apple", "banana", "cherry", "date", "elderberry"]?
# list1 = ["apple", "banana", "cherry", "date", "elderberry"]
# print(list1)
#
# # 6.How do you access the second and fourth elements from the list.
# print(list1[1],list1[3])

# 7.Modify the third element in the list numbers = [10, 20, 30, 40, 50] to 35
# mylist = [10, 20, 30, 40, 50]
# print(mylist)
# # print(mylist.insert(2, 35))
# print(mylist.remove(30), mylist.insert(2,35))
# print(mylist)

# Alternate method
# mylist[2] = 35
# print(mylist)

# Create a Tuple
# t = ("red", "green", "blue")
# print(t)

# Access Elements in a Tuple
# t2 = ("red", "green", "blue", "yellow")
# print(t2[0])
# print(t2[-1])

# Immutable Nature of Tuples:
# What happens if you try to change the second element of the tuple colors = ("red", "green", "blue")?-
# it will not allow any changes in tuple

# Tuple Unpacking
# t = (10, 20, 30)
# print(t)
# for i in t:
#     print(i)
#
# # Check Element in Tuple:
# t = ("red", "green", "blue")
# if "blue" in t:
#     print("blue is present")
# else:
#     print("blue is not present")

# Tuple Length

# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# print(len(days))

# Create a Dictionary
# d = {"Alice": 85, "Bob": 90, "Charlie": 78}

# print(d)

# Access Dictionary Values
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
#
# Bob_index = students["Bob"]
#
# print(Bob_index)

# Add and Remove Key-Value Pairs
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# print(students)
# students["David"] = 92
# print(students)
# del students["Charlie"]
# print(students)

# Update Dictionary Values
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# print(students)
# students["Bob"] = 95
# print(students)

# Check if Key Exists in a Dictionary
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# if "Alice" in students:
#     print("Alice is exist")
# else:
#     print("Alice is not exist")


# Dictionary Length
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# print(len(students))