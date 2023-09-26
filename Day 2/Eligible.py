n = input("Enter your name")
g = input("Enter your gender. M for male and F for female")
a = int(input("Enter age"))
if (n.startswith("M") or n.startswith("m")) and (g.startswith("M") or g.startswith("m")):
    print(n, " is going to become a father")
elif (n.startswith("a") or n.startswith("A")) and (g.startswith("F") or g.startswith("f")):
    print(n, " is going to become a housewife")
else:
    if a > 18:
        print(n, " is eligible to vote")
    else:
        print(n, " is not eligible to vote")
