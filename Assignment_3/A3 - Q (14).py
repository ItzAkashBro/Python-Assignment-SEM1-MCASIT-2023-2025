# A machine is purchased which will produce earning of Rs. 1000 per year while it lasts. The
# machine costs Rs. 6000 and will have a salvage of Rs. 2000 when it is condemned. If 12
# percent per annum can be earned on alternate investments what would be the minimum life of
# the machine to make it a more attractive investment compared to alternative investment?

year = 0
invest = 0
alternate = 0
while alternate <= invest:
    year += 1
    alternate = year * 90
    invest = (1000 * year) - 4000
print(f"The Life of Machine: {year} years")