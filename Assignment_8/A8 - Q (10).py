# Write a Python program to print a dictionary in table format.

d = {'Name': 'John', 'Age': 25, 'City': 'New York', 'Grade': 'A'}
print("{:<15} {:<15}".format('Key', 'Value'))
print("="*30)
for key, value in d.items():
    print("{:<15} {:<15}".format(str(key), str(value)))