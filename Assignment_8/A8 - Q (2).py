# Write a Python script to check whether a given key already exists in a dictionary.

dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
check=int(input("Enter the key value that you want to check:"))
if check in dic:
    print("2. Key exists in dictionary.")
else:
    print("2. Key does not exist in dictionary.")
print()