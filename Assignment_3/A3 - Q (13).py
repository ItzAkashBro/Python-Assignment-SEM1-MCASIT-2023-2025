# Write a program to generate all combinations of 1, 2 and 3 using for loop.

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if(i!=j and i!=k and j!=k):
                print(i,j,k)