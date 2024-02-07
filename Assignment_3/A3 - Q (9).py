# Write a program to print all prime numbers from 1 to 300.
# (Hint: Use nested loops, break and continue)

num = 2
for i in range(1, 300):
 j= 2
 while ( j <= (i/2)):
  if (i % j == 0): 
   break 
  j += 1
 if ( j > i/j) : 
  print ( i, "is a prime number")