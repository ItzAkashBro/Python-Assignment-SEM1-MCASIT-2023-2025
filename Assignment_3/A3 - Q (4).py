# Write a program to print all the ASCII values and their equivalent characters using a while loop.

ascii_value = 0
while ascii_value <= 255:
    character = chr(ascii_value)
    ascii = ord(character)
    print(f"ASCII Value: {ascii}, Character: {character}")
    ascii_value += 1
