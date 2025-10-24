# Exercise 1: Calculation of Area of Rectangle, Square, Circle and Trapezium.
import os  
os.system('cls' if os.name == 'nt' else 'clear')
#-----------------
# Rectangle:
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))

# areaRec = length * width

# print(f"The area of the rectangle is: {areaRec}")
#-----------------
# Square:
# length = float(input("Enter the length of one side of a square: "))

# areaSqre = length ** 2

# print(f"The area of the square is: {areaSqre}")
#-----------------
# Circle:
# pi = 3.142
# radius = float(input("Enter the radius of a circle: "))

# areaCirc = pi*(radius**2)

# print(f"The area of a circle is: {areaCirc}")
#-----------------
# Trapezium:
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b or base: "))
height = float(input("Enter height: "))

areaTrap = (0.5 * (a+b)) * height

print(f"The area of the trapezium is: {areaTrap}")


