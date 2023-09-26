def add(m, n):
    print("Sum= ", m + n)


def sub(m, n):
    print("Difference= ", m - n)


def mul(m, n):
    print("Product= ", m * n)


def div(m, n):
    print("Quotient= ", m / n)


a = int(input("Enter the 1st no."))
b = int(input("Enter the 2nd no."))
c = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division"))
if c == 1:
    add(a, b)
elif c == 2:
    sub(a, b)
elif c == 3:
    mul(a, b)
elif c == 4:
    div(a, b)
else:
    print("Invalid")
