# is operatörü
x = y = [1,2,3]
z = [1,2,3]

print (x == y)  # True
print (x == z)  # True

print (x is y)  # True
print (x is z)  # False farklı adreslere sahip olduklarından farklı nesneler olarak algılanır.
print ( x is not z)

# in operatörü
lists = ["apple", "banana", "cherry"]

print ("apple" in lists)
print ("banana" not in lists)
