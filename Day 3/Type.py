l1 = [True, False, [1, 2, 3], 1, 2.0, 3]
l = [str(i) for i in l1 if type(i) == int or type(i) == float]
print(l)

# l = []
# for i in l1:
# if type(i) == int or type(i)==float:
# l.append(str(i))
