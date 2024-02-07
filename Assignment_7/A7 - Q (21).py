# Write a Python function that checks whether a passed string is palindrome or not.

def pal(str):
    c = ''.join(char.lower() for char in str if char.isalnum())
    return c == c[::-1]
s= "A man, a plan, a canal, Panama"
print(f'"{s}" {"is" if pal(s) else "is not"} a palindrome.')