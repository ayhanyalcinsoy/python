#"Bmw", "Mercedes", "Opel", "Mazda"  elamanlarına sahip liste oluştur.
list = ["Bmw", "Mercedes", "Opel", "Mazda"]
print (list)
# Liste kaç elemanlıdır.
elamanSayi = len(list)
print("Listenin eleman sayısı:", elamanSayi)

#Listeinin ilk ve son elemanları
firstE = list[0]
lastE =list[-1]
print (f"Listenin ilk elemanı '{firstE}' ve son elemanı '{lastE}'.")

#Mazda yerine Toyota yazdır
liste1 = list
liste1[3] = "Toyota"
print (liste1)

#Mercedes listenin bir elemanımıdır
isFound = list.index('Mercedes')
print (isFound)

#Listenin -2 indeksinin değeri nedir
eksiIki = list[-2]
print (eksiIki)

#listenin ilk üç elemanı
firstThree = list[:3]
print (firstThree)

#Listenin son 2 elamanı yerine Toyota ve Renault ekleyin
list[-2] = "Toyota"
list[-1] = "Renault"
print (list)

#listenin üzerine Audi ve Nissan ekleyin
list1 = ["Audi", "Nissan"]
list.extend(list1)
print(list)

#son elemanı sil
list.pop(-1)
print(list)

#tersten  yazdır
list.reverse()
print(list)

#Aşağıdaki verileri liste içinde sakla:
  #studentA = Yiğit Bilgi, 2010, (70,60,70)
  #studentB = Sena Turan, 1999, (80,80,70)
  #studentC = Ahmet Turan, 1998, (80,70,90)

studentA = ["Yiğit Bilgi", 2010, "(70,60,70"]
studentB = ["Sena Turan", 1999, "(80,80,70)"]
studentC = ["Ahmet Turan", 1998, "(80,70,90)"]

print (studentA)
print (studentB)
print (studentC)

students = [studentA, studentB, studentC]
print (students)
print ("Listenin son elemanı :",students[-1])
