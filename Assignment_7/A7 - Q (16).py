# Write a Python function that accepts a string and calculate
# the number of upper case letters and lower case letters.

def culc(input_string):
    return sum(1 for char in input_string if char.isupper()), sum(1 for char in input_string if char.islower())
str = "Hello, World!"
upper, lower = culc(str)
print(f"Upper case letters: {upper}, Lower case letters: {lower}")