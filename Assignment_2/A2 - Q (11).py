# Given the coordinates (x, y) of a center of a circle and it’s radius, write a program which will
# determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use
# sqrt( ) and pow( ) functions)

import math
def point_circle_relationship(x_c, y_c, radius, x_p, y_p):
    distance = math.sqrt((x_p - x_c)**2 + (y_p - y_c)**2)
    return "Inside" if distance < radius else "On" if distance == radius else "Outside"
center_x, center_y, radius = map(float, input("Enter center coordinates (x y) and radius: ").split())
point_x, point_y = map(float, input("Enter point coordinates (x y): ").split())
print(point_circle_relationship(center_x, center_y, radius, point_x, point_y))