#If cost price and selling price of an item is input through the keyboard,
#write a program to determine whether the seller has made profit or incurred loss.
#Also determine how much profit he made or loss he incurred.
 
CostPrice=int(input("Enter The Cost Price:- "))
SellingPrice=int(input("Enter The Selling Price:- "))
if SellingPrice>CostPrice:
    print("You Made Profit of:- ",SellingPrice-CostPrice)
else:
    print("You Made Loss of :- ",CostPrice-SellingPrice)