# Write a program to  convert numeric words to numbers

w = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
s = input("Enter a string with numeric words: ")
c = ' '.join(str(w.get(word.lower(), word)) for word in s.split())
print("Original String:", s)
print("After converting numeric words to numbers:", c)