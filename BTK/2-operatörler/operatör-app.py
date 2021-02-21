x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# Kullanıcıdan alınan iki sayı ile x,y,z sayılarının toplamı farkı nedir

a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))

result = (a * b) - (x + y + z)
print(result)

#y'nin x'e kalansız bölümü
bolum = y // x
print(bolum)

#x,y,z toplamının mod 3'ü nedir?
mod3 = (x + y +z) % 3
print (mod3)

#y'nin x kuvveti
kuvvet = y ** x
print(kuvvet)

#x, *y, z = numbers işlemine göre z'nin küpü kaçtır

x, *y, z = numbers
print (z**3)

#x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır.
yToplam = y[0] + y[1] + y[2]
print(yToplam)
