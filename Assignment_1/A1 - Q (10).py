# In a town, the percentage of men is 52. The percentage of total literacy is 48.
# If total percentage of literate men is 35 of the total population,
# write a program to find the total number of illiterate men and women if the population of the town is 80,000.

TotalPopulation=80000
Men=TotalPopulation*(52/100)
LiterateMen=TotalPopulation*(35/100)
TotalLiteracy=TotalPopulation*(48/100)
LiterateWomen=TotalLiteracy-LiterateMen
print(f"Total Literacy of the Town is {TotalLiteracy}, Literate men in the town is {LiterateMen} and Literate Women is {LiterateWomen}")