#value types => string, number

x = 5
y = 25

x = y
y = 20

print(x,y)

#reference types => list, class

a = ['apple', 'banana']
b = ['apple', 'banana']

a = b

b[0] = 'grape'  # Bu değişiklik a değişkenini de etkiler

print(a, b)
