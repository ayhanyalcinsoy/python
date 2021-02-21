x, y, z = 10, 16, 20

x += 5  # x = x + 5
x -= 5  # x = x - 5
x *= 5  # x = x * 5
x /= 5  # x = x / 5
x %= 5  # x = x % 5
y //= 5  # y = y // 5
y **= 5  # y = y ** 5

print(x,y,z)

print ('*'*50)
values = 1, 2, 3, 4, 5

print (values)
print (type(values))

x, y, *z = values #x,y,z değişkenlerine karşılık gelen değeri atar yoksa hata verir.
# *z x ve y karşılığı değerler atandıktan sonra kalanlar z'ye liste olarak atanır
print(x,y,z)
print (x,y,z[2]) #indeks ile z'nin elemanlarına ulaşılabilir
