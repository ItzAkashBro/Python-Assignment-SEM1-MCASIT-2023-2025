# If a five-digit number is input through the keyboard,
# write a program to print a new number by adding one to each of its digits.
# For example if the number that is input is 12391 then the output should be displayed as 23402.

num=int(input("Enter 5 digit number:"))
print("New Number is: ")
print(((num//10000)+1)%10,end='')
print(((num//1000)+1)%10,end='')
print(((num//100)+1)%10,end='')
print(((num//10)+1)%10,end='')
print(((num%10)+1)%10,end='')