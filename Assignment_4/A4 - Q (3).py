# Write a program in C to calculate sum of Fibonacci series.

limit=int(input('Enter a limit:'))
sum=0
a=0
b=1
while limit>0:
    temp=a+b
    a=b
    b=temp
    limit-=1
    print(temp,' ')
    sum=sum+temp
print('Sum of the series: ',sum)