# Given the length and breadth of a rectangle, write a program to find whether the area of the
# rectangle is greater than its perimeter. For example, the area of the rectangle with length = 5
# and breadth = 4 is greater than its perimeter.

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
if length * breadth > 2 * (length + breadth):
    print("The area of the rectangle is greater than its perimeter.")
elif length * breadth < 2 * (length + breadth):
    print("The area of the rectangle is less than its perimeter.")
else:
    print("The area and perimeter of the rectangle are equal.")