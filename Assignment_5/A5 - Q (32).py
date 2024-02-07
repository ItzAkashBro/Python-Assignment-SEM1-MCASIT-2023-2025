# Write a program to sort String list by K character frequency

sl = input("Enter a list of strings separated by space: ").split()
k = int(input("Enter the value of K: "))
ss = sorted(sl, key=lambda s: s.count(s[k-1]))
print("Sorted String List:")
print(ss)