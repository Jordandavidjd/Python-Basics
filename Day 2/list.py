m1 = ["Jan", "Feb", "Mar"]
m2 = ["Apr", "May"]
months = m1 + m2
print(months)
for m in m2:
    print(m)
mn = [1, 2, 3, 4, 5]
for i in mn:
    print(i, "-", months[i - 1])
m3 = "june"
months.append(m3)
print(months)
m4 = ["june", "july", "august"]
months.extend(m4)
print(months)
months.pop()
print(months)
months.pop(2)
print(months)
print(months.count("june"))
months.remove("june")
print(months)
print(len(months))
