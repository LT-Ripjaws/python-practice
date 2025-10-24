# Exercise -3: Calculating the circumference of a circle, Area of a circle, Hypotenuse of a right triangle using math functions
import os
import math
os.system('cls' if os.name == 'nt' else 'clear')
#--------------
# Circumference:

# We know the formula is C = 2*pi*r
# radius = float(input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius

# print(f"The circumference of the circle is: {round(circumference, 2)}")
#--------------
# Area:
# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * pow(radius,2)

# print(f"The area of the circle is: {round(area, 2)}")
#--------------
# Hypotenuse:
a = float(input("Enter side a/height: "))
b = float(input("Enter side b/base: "))

c = math.sqrt(pow(a,2)+pow(b,2))

print(f"The hypotenus is: {c}")
#--------------