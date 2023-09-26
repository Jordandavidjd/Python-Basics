def small(l):
    s = l[0]
    m = l[0]
    for i in l:
        if i < s:
            s = i
        if i > m:
            m = i
    return s, m


l1 = [-3, 7, 6, 5, 2, -9]
min,max = small(l1)

print(f"Smallest no.- {min}")
print(f"Largest no.- {max}")

# def small(l)
# l.sort()
# return l[0]
