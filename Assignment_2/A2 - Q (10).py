# Given three points (x1, y1), (x2, y2) and (x3, y3),
# write a program to check if all the three points fall on one straight line.
 
x1, y1 = map(float, input("Enter coordinates of point 1 (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of point 2 (x2 y2): ").split())
x3, y3 = map(float, input("Enter coordinates of point 3 (x3 y3): ").split())
m = (y2 - y1) / (x2 - x1)
n = (y3 - y2) / (x3 - x2)
if m == n:
    print("All 3 points lie on the same line.")
else:
    print("All 3 points do not lie on the same line.")