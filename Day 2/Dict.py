usn = {
    'name': "Shwetha",
    'age': 20,
    'usn': "1at20ec139",
}
# to add elements
usn['location'] = "Kumarapark"
more = {'food': "pizza", 'college': "Atria"}
usn.update(more)

# to print key and value
for i, j in usn.items():
    print(i, " - ", j)

# to delete item
usn.pop('food')
print(usn)

# to print only key
# for key in usn.keys(): or for key in usn:
# print(key)
# to print only values
# for value in usn.values():
# print(value)
