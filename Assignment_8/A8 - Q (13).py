# Write a Python program to create a dictionary of keys x, y, and z where each key has as value
# a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the
# dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]

dd = {'x': list(range(11, 20)), 'y': list(range(21, 30)), 'z': list(range(31, 40))}
x = dd['x'][4]
y = dd['y'][4]
z = dd['z'][4]
print(dd)
print(x)
print(y)
print(z)
for key, value in dd.items():
    print(f"{key} has value {value}")