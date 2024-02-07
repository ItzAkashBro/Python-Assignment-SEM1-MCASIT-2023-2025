# Write a program to check whether a triangle is valid or not, when the three angles of the
# triangle are entered through the keyboard. A triangle is valid if the sum of all the three
# angles is equal to 180 degrees.

angle1 = int(input("Enter the first angle in degrees: "))
angle2 = int(input("Enter the second angle in degrees: "))
angle3 = int(input("Enter the third angle in degrees: "))

if (angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0):
    print("The angles form a valid triangle.")
else:
    print("The angles do not form a valid triangle.") 