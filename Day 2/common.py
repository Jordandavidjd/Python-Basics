l1 = ["a", "b", "c"]
l2 = ["b", "c", "d"]
l3 = l1 + l2
c = []
for i in l3:
    co = l3.count(i)
    if co > 1:
        c.append(i)
        l3.remove(i)
print("Common elements-", c)
