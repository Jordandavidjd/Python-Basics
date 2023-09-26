import random

c = [0, 1, 2]
comp = random.choice(c)
n = int(input("Enter 0 for rock, 1 for paper and 2 for scissors"))
if n < 0 or n > 2:
    print("Wrong input")
    n = int(input("Enter 0 for rock, 1 for paper and 2 for scissors"))
if n == 0:
    print("You played rock")
elif n == 1:
    print("You played paper")
else:
    print("You played scissors")
if comp == n:
    print("Draw")
elif comp == 0:
    print("Computer played rock")
    if n == 1:
        print("You win")
    else:
        print("You lose")
elif comp == 1:
    print("Computer played paper")

    if n == 2:
        print("You win")
    else:
        print("You lose")
else:
    print("Computer played scissors")
    if n == 0:
        print("You win")
    else:
        print("You lose")
