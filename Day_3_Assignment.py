# 1. Write a Python function to find the maximum of three numbers
# numbers = [3, 5, 6,]
# print(f"Max : {max(numbers)}")



# 2.Write a Python function to multiply all the numbers in a list.
# numbers = [8, 2, 3, -1, 7]
# def multiply_list(numbers):
#     product = 1
#     for i in numbers:
#         product *= i
#     return product
# product = multiply_list(numbers)
# print(product)

# 3.Write a Python program to reverse a string.
# st = "1234abcd"
# def reverse(st):
#     str = ""
#     for i in st:
#         str = i + str
#     return str
# print("The original string is : ", end="")
# print(st)
#
# print("The reversed string is : ", end="")
# print(reverse(st))

# 4. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# n = int(input("Enter a non-negative number is:"))
# print(factorial(n))

# 5. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# list1 = [1, 2, 3, 3, 3, 3, 4, 4, 5, 0, 0]
# def unique_list(list1):
#     x = []
#     for n in list1:
#         if n not in x:
#             x.append(n)
#     return x
# print(unique_list(list1))

# 6.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# def prime_num (n):
#     if (n == 1):
#         return print("It is not a prime number", n)
#
#     elif (n == 2):
#         return print("It is not a prime number", n)
#
#     else:
#         for x in range (3, n):
#             if (n % x == 0):
#                 return print("It is not a prime number", n)
#
#         return print("It is a prime number", n)
#
# prime_num (39)

# 7.Write a Python program to print the even numbers from a given list.

# def even_num(list):
#     # create an empty list
#     enum = []
#
#     for n in list:
#         if n == 0 or n % 2 == 0:
#             enum.append(n)
#
#     return enum
#
# print(even_num([0,1,2,3,4,5,6,7,8,9,10,11]))

# 8.Write a Python function that accepts a string and counts the number of upper and lower case letters.

# def string_check(s):
#     # create a distionary 'd' to store the upper and lower char count
#     d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
#     for c in s:
#         if c.isupper():
#             d["UPPER_CASE"]+= 1
#         elif c.islower():
#             d["LOWER_CASE"]+=1
#         else:
#             pass
#     print("orginal string: ", s)
#
#     print("number of upper case character: ", d["UPPER_CASE"])
#     print("number of lower case character: ", d["LOWER_CASE"])
# string_check('My Name is Mahendra Singh')

# 9.Write a Python function to sum all the numbers in a list.
# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#
#     return total
#
# print(sum((8,2,3,0,7,0,1)))

# 10.Write a Python function that checks whether a passed string is a palindrome or not.
# def isPalindrome(str):
#
#     left_pos = 0
#     right_pos = len(str) -1
#
#     while left_pos < right_pos:
#         if str[left_pos] != str[right_pos]:
#             return False
#         left_pos += 1
#         right_pos -= 1
#     return True
# print(isPalindrome('ana'))


