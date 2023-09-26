def add(m, n):
    print("Sum= ", m + n)


def sub(m, n):
    print("Difference= ", m - n)


def mul(m, n):
    print("Product= ", m * n)


def div(m, n):
    print("Quotient= ", m / n)


s = input("Enter the expression in the format a+b")
sym = ["+", "-", "*", "/"]
for i in range(4):
    c = s.find(sym[i])
    if c > 0:
        break
a = int(s[0:c])
b = int(s[c + 1::])
if s[c] == "+":
    add(a, b)
elif s[c] == "-":
    sub(a, b)
elif s[c] == "*":
    mul(a, b)
elif s[c] == "/":
    div(a, b)
else:
    print("Invalid operator")
