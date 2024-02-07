# If the three sides of a triangle are entered through the keyboard, write a program to check
# whether the triangle is valid or not. The triangle is valid if the sum of two sides is greater
# than the largest of the three sides.

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")
