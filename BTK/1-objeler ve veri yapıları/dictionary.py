ogrenciler = {}

number = input ("Öğrenci No: ")
name = input("Öğrenci Adı: ")
surname = input("Öğrenci Soyadı: ")
score = input ("Aldığı Not: ")

ogrenciler.update({
  number:{
    'adi': name,
    'soyadi': surname,
    'notu': score

  }
  
})
number = input ("Öğrenci No: ")
name = input("Öğrenci Adı: ")
surname = input("Öğrenci Soyadı: ")
score = input ("Aldığı Not: ")

ogrenciler.update({
  number:{
    'adi': name,
    'soyadi': surname,
    'notu': score

  }
  
})

#print(ogrenciler)
print ("*"*50)
ogrNo= input("Öğrenci Numarası:")
ogrenci = ogrenciler[ogrNo]

print(f"{ogrNo} nolu ve {ogrenci['adi']} {ogrenci['soyadi']} isimli öğrenci sınavdan {ogrenci['notu']} almıştır")
