# Program to find the differences of two lists.

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
d = list(set(l1) - set(l2))
print("Differences between List 1 and List 2:", d)