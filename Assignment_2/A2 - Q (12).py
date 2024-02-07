# Given a point (x, y), write a program to find out if it lies
# on the x-axis, y-axis or at the origin, viz. (0, 0)

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))
if x == 0 and y == 0:
    print("The point is at the origin (0, 0)")
elif x == 0:
    print(f"The point ({x}, {y}) lies on the y-axis")
elif y == 0:
    print(f"The point ({x}, {y}) lies on the x-axis")
else:
    print(f"The point ({x}, {y}) does not lie on the x-axis, y-axis, or at the origin")
