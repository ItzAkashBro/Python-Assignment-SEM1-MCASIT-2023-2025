# Write a program to find words that are greater than the given length k

def wgk(input_str, k):
    w = input_str.split()
    r = [word for word in w if len(word) > k]
    return r
input_str = input("Enter a string: ")
k = int(input("Enter the minimum length of words to find: "))
rw = wgk(input_str, k)
print(f"Words greater than length {k}: {rw}")