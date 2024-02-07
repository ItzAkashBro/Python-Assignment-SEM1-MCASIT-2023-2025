# If the three sides of a triangle are entered through the keyboard, write a program to check
# whether the triangle is isosceles, equilateral, scalene or right angled triangle.

side1=int(input("Enter for Side 1: "))
side2=int(input("Enter for Side 2: "))
side3=int(input("Enter for Side 3: "))
if side1==side2==side3:
    print("Equilateral Triangle")
elif side1==side2 or side2==side3 or side1==side3:
    print("isosceles triangle")
elif(side1*side1)+(side2*side2)==(side3*side3) or (side2*side2)+(side3*side3)==(side1*side1) or (side1*side1)+(side3*side3)==(side2*side2):
    print("Right Angeled Triangle")
else:
    print("scalene trangle")