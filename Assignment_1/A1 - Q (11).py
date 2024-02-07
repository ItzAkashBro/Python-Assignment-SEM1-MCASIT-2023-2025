# A cashier has currency notes of denominations 10, 50 and 100.
# If the amount to be withdrawn is input through the keyboard in hundreds,
# find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.

amount=int(input("Enter Amount To Withdraw(in Hundreds):- "))
print("100 Notes: ",amount//100)
print("50 Notes: ",(amount%100)//50)
print("10 Notes: ",((amount%100)%50)//10)
print("Remaining Amount: ",((amount%100)%50)%10)