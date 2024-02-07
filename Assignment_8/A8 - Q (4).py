# Write a Python program to iterate over dictionaries using for loops.

dic = {1: 10, 2: 20, 3: 36, 4: 40, 5: 52, 6: 60}
print("Iterating over keys:")
for key in dic:
    print(key)
print("\nIterating over values:")
for value in dic.values():
    print(value)
print("\nIterating over key-value pairs:")
for key, value in dic.items():
    print(f"{key}: {value}")
