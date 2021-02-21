names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998,2000,1998,1987]

#Cenk ismini listenin sonuna ekleyin
names.append("Cenk")
print (names)
#Sena değerini listenin başına ekleyin
names.insert(0, "Sena")
print (names)
#Deniz ismini listeden silin
names.remove("Deniz")
print (names)
#Ali listenin bir elemanı mıdır?
search = "Ali" in names
print (search)
#liste elemanlarını ters çevirin
names.reverse()
print(names)
#Liste elemanlarını alfabetik olarak sıralayın
names.sort()
print(names)
names.sort(reverse=True)
print(names)
#years listesini rakamsal büyüklüğe göre sıralayın
years.sort()
print (years)

#str = "Chevrolet, Dacia" dizisini karakter listesine çevirin
stir = "Checrolet, Dacia"
char_stir = stir.split(",")
print (char_stir)
#years dizisinin enbüyük ve en küçük elemanı nedir
eB = max(years)
eK = min(years)
print (f"{eB} 'years' dizisinin en büyük değeri, {eK} ise en küçük değeridir")
#years dizisinde kaç tane 1998 elamanı vardır
say = years.count(1998)
print (say)
#years dizinin tüm elemanlarını silin
years.clear()
print (years)
#kullanıcıdan alacağınız üç tane marka bilgisini bir listede saklayın

markalar = []
marka = input("Bir marka girin: ")
markalar.append(marka)

marka = input("Bir marka girin: ")
markalar.append(marka)

marka = input("Bir marka girin: ")
markalar.append(marka)

print(markalar)

