# 1.Write a Python program to create a class named Car
# Define attributes like brand, model, and year.
# Create an object of the class and display the details of the car?
from encodings.punycode import selective_len


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#
# my_car = Car("Suzuki", "Fronx", "2023")
# print(f"Car Details: Brand:{my_car.brand}, Model:{my_car.model}, Year:{my_car.year}")

# 2.Create a class Student with attributes name, roll_number, and marks.
# Define a constructor to initialize these attributes
# # and a method display_info() to print the student's details?
# class student:
#     def __init__(self,name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks
#     def display_info(self):
#         print(f"Name:{self.name}, \nRoll number:{self.roll_number}, \nMarks:{self.marks}")
# #Creating an object of the Student
# S1 = student("Mahendra", 113, 99)
# #
# # # Displaying the student's
# S1.display_info()

# 3. Create a class Rectangle with attributes length and breadth.
# Include methods to calculate the area and perimeter of the rectangle.
# Create multiple objects and display the area and perimeter for each?

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        return self.length * self.width

    def rectangle_perimeter(self):
        return 2 * (self.length + self.width)

# length = int(input("Enter Length is: "))
# width = int(input("Enter Width is: "))

r1 = Rectangle(4,3)
print("Rectangle object Details are:")
# r1.display_data()
# print("")
# print(new_rect.rectangle_area(), new_rect.rectangle_perimeter())
print("Area of Rectanle is: ",r1.rectangle_area())
# print("")
print("Paerimeter of Rectangle is:", r1.rectangle_perimeter())

# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius =radius
#     def get_area(self):
#         return math.pi*(self.radius**2)
#     def get_circumference(self):
#         return 2*math.pi*self.radius
#
# if __name__ == "__main__":
#         circle = Circle(5)
#         print("Area:", circle.get_area())
#         print("Circumference:", circle.get_circumference())


def display_data(self):
    print(f'l:{self.length}, w:{self.width}')