# Program to sort the elements of given list in Ascending and Descending Order.

l = [5, 2, 8, 1, 7, 3, 9, 4, 6]
a, d = sorted(l), sorted(l, reverse=True)
print("Original List:", l)
print("Ascending Order:", a)
print("Descending Order:", d)