# Write a program for a matchstick game being played between the computer and a user.
# Your program should ensure that the computer always wins. Rules for the game are as follows:
# - There are 21 matchsticks.
# - The computer asks the player to pick 1, 2, 3, or 4 matchsticks.
# - After the person picks, the computer does its picking.
# - Whoever is forced to pick up the last matchstick loses the game.

m = 21
print("Matchstick Game!")
while m > 0:
    up = int(input("Your turn: Pick 1, 2, 3, or 4 matchsticks: "))
    m -= up
    print(f"Remaining matchsticks: {m}")
    if m == 0:
        print("You picked the last matchstick. Computer wins!")
        break
    cp = 5 - up
    m -= cp
    print(f"Computer's turn: Computer picks {cp} matchsticks. Remaining matchsticks: {m}")
    if m == 0:
        print("Computer picked the last matchstick. You lose!")