# Write a program to find all close matches of input string from a list

from difflib import get_close_matches
word_list = ["apple", "banana", "cherry", "date", "grape", "orange", "pear"]
input_string = input("Enter a word: ")
close_matches = get_close_matches(input_string, word_list)
print(f"Close matches for '{input_string}': {close_matches}")