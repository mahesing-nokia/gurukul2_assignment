# Convert any Float variable to Int Data type:
# a = 3.2
# print(a, type(a))
# print("Class type of a is ", type(int(a)))
# b = 'Average is '
# c = b + str(a)
# print(c)


# Write a program to read 2 numbers from the keyboard and print sum Special operators
# x = input("Enter the first number is :")
# y = input("Enter the second number is :")
# print("sum is : ", (int(x) + int(y)))

# name = input("Enter your name is :")
# if name == "mahi":
#     print("Hello Good Morning ", name + " !")
# print("Hi")

# Write a Program to find Maximum of 3 Numbers
# a = int(input("Enter First Number:"))
# b = int(input("Enter Second Number:"))
# c = int(input("Enter Third Number:"))
# if a > b and a > c:
#     print("max num is a", a)
# else:
#     if b > c:
#         print("max is b", b)
#     else:
#         print("max is c", c)

# Write a Program to find Biggest of given 2 Numbers from the Key Board?
# n1 = int(input("Enter first number:"))
# n2 = int(input("Enter second number:"))
# if n1 > n2:
#     print("Biggest number is :", n1)
# else:
#     print("Biggest number is :", n2)

# Write a Program to Check whether the given Number is in between 1 and 10?
# num = int(input("Enter Number :"))
# if num>=1 and num<=10:
#     print("The number", num ,"is in between 1 and 10")
# else:
#     print("The number", num ,"is not between 1 and 10")

# Question 1: Write a Python program that takes two numbers as input from the user and performs the following operations:
# a = int(input("Enter the first number is :"))
# b = int(input("Enter the second number is :"))
# # Addition
# print("The addition of a and b is : ", a + b)
# # Subtraction
# print("The subtraction of a and b is : ", a - b)
# # Multiplication
# print("The multiplication of a and b is : ", a * b)
# # Division
# print("The division of a and b is : ", a / b)
# # Modulus
# print("The modulus of a and b is : ", a % b)

# Question 2: Write a Python program that checks whether a given number is even or odd using the modulus operator.
# a = int(input("Enter the number is :"))
# if a % 2 == 0:
#     print("a is even number")
# else:
#     print("a is odd number")

# Question 3: Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero.
# a = float(input("Enter the number is :"))
# if a < 0:
#     print("number is negative")
# else:
#     if a > 0:
#         print("number is positive")
#
# if a == 0:
#     print("number is equal to zero")

# Question 4: Write a Python program that calculates the grade of a student based on the marks entered by the user. The grading scale is as follows:
# n = float(input("enter the marks obtained is :"))
# if n >=90 and n <= 100:
#     print("grade of student is A")
# if n >= 80 and n <=89:
#     print("grade of student is B")
# if n >= 70 and n <=79:
#     print("grade of student is C")
# if n >= 60 and n <=69:
#     print("grade of student is D")
# if n < 60:
#     print("grade of student is F")

# Question 5: Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.
# with open("sample1.txt", "w") as f:
#     f.write("This is my new sample file.\n")
#     f.write("Very nice file created.")
# with open("sample1.txt", "r") as f1:
#     data = f1.read()
#     print(data)

# Question 6: Write a Python program that reads a text file called data.txt and counts the number of words in the file.
# with open("data.txt", "w") as f:
#     f.write("This is my first program in python.")
# with open("data.txt", "r") as f:
#
#     data = f.read()
#     print(data)
# file = open("data.txt", "r")
# count  = 0
# for line in file:
#     words = line.split(" ")
#     count +=len(words)
# f.close()
# print("Number of words in data file is :", count)

# Question 7: Write a Python program to print the numbers from 1 to 10 using a for loop.
# for x in range(0,10):
#     print(x+1)
# # alternate method
# for x in range(1,11):
#     print(x)

# Question 8: Write a Python program to display the multiplication table of a number entered by the user using a for loop.
# x = int(input("Enter the number :"))
# for i in range(1,11):
#     j = i*x
#     print(j)