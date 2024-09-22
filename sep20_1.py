# s = [1, 2, 3, 4, 5]
#
# # s[1] = 0
# print(s, type(s))
# s.append(45)
# print(s.__len__())
# print(s)
# s.pop(2)
# print(s)
# s.append(6)
# print(s)
# s.insert(1,9)
# print(s)
# a = 7
# b = 3.0
# c = a + b
# print(c, type(c))
# n = a + int(b)
# print(n, type(n))
# a = 5.9
# b = 5
# c = int(a) + int(b)
# print(c, type(c))
a = 10
b = 12

# print("a > b is ", a > b)
# print("a = b is", a == b)
# print("a != b is ", a != b)
#
# a = True
# b = False
# # print(a and b)
# # print(a or b)
# print(not (a, b))

# x = input("Enter the value of a is ")
# print(x)

# x=input("Enter First Number:")
# y=input("Enter Second Number:")
# # i = int(x)
# # j = int(y)
# c = x + y
# print("The Sum:", c)


# eno = int(input("Enter Employee No:"))
# ename = input("Enter Employee Name:")
# esal = float(input("Enter Employee Salary:"))
# eaddr = input("Enter Employee Address:")
# married = bool(input("Employee Married ?[True|False]:"))
# print("Please Confirm Information")
# print("Employee No :", eno)
# print("Employee Name :", ename)
# print("Employee Salary :", esal)
# print("Employee Address :", eaddr)
# print("Employee Married ? :", married)
# print(type(ename))
# x = 3
# while x < 10:
#     print(x)
#     x= x+1
for i in range(10):
    if i%2 ==0:
        continue
    print(i)