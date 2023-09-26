l1 = ("a", "b", "c")
l2 = ("b", "c", "d")
l3 = l1 + l2
print(l3)
c = ()
for i in l3:
    co = l3.count(i)
    if co > 1:
        ind = l3.index(i)
        l: tuple = tuple(l3[ind])
        if l3[ind] not in c:
            c = c + l
print("Common elements-", c)
