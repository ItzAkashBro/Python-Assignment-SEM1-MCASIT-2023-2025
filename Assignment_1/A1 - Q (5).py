# The length & breadth of a rectangle and radius of a circle are input through the keyboard.
# Write a program to calculate the area & perimeter of the rectangle, and the area & circumference of the circle.

import math
Length=float(input("Enter The length:-\n"))
Breadth=float(input("Enter The Breadth:-\n"))
Radius=float(input("Enter The radius of a circle:-\n"))
print("The Area of the rectangle is:- ",Length*Breadth)
print("The perimeter of the rectangle is:- ",2*(Length+Breadth))
print("Area Of the Circle is:-",math.pi*(Radius*Radius))
print("circumference Of the Circle is:-",2*(math.pi*Radius))

