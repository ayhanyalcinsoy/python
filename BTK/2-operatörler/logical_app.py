#Girilen bir sayının 0-100 arasında olup olmadığını kontrol et
"""
sayi = float(input("Bir sayı giriniz: "))
araSayi = (sayi>0) and (sayi<=100)
print (f"Girdiniz {sayi} sayısı, 0-100 arasındadır: {araSayi}")
#Girilen bir sayının pozitif çift sayı olup olmadığını kontrol et
ciftmi = (sayi>=0) and (sayi%2==0)
print(f"Girdiğiniz sayı pozitif ve çift sayıdır: {ciftmi}")
"""
# email ve parola bilgileri ile giriş kontrolü
"""
email = "email@pisilinux.org"
passw = "abc123"

yourEmail = input("E-posta adresini giriniz: ")
yourPassw = input("Parolanızı giriniz: ")

succesLogin = (yourEmail == email) and (yourPassw == passw)
print (f"Başarılı bir giriş yaptınız: {succesLogin}")
"""
# Girilen 3 sayının büyüklük olarak karşılaştırılması
"""
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

aBuyuk = (a>b) and (a>c)
bBuyuk = (b>a) and (b>c)
cBuyuk = (c>a) and (c>b)

print (f"{a} sayısı {b} ve {c} sayılarından büyüktür: {aBuyuk}")
print (f"{b} sayısı {a} ve {c} sayılarından büyüktür: {bBuyuk}")
print (f"{c} sayısı {a} ve {b} sayılarından büyüktür: {cBuyuk}")
"""
#Kullanıcıdan 2 vize (%60) ve bir final notu
    # 50 ve üzeri ise geçti değilse kaldı.
    # Ortalama 50 bile olsa finalden enaz 50 almalı
    # Finalden 70 aldığında ortalamanın önemi olmasın
vize1 = float(input("Vize1: "))
vize2 = float(input("Vize2: "))
final = float(input("Final: "))

ortalama = (((vize1+vize1)/2)*0.6) + (final*0.4)
succes = ((ortalama >= 50) and (final >= 50)) or (final >= 70)

print(f"Not ortalamanız {ortalama} ve ders geçme durumunuz: {succes}")

# Kişinin ad, kilo ve boy bilgileri ile kilo endeksini hesapla
   # 0-18.4 => Zayıf
   # 18.5-24.9 => Normal
   # 25.0 - 29.9 => Kilolu
   # 30.0-34.9 => Aşırı kilolu (Obez)
"""
name = input ("Adınız: ")
kg = float(input("Kilonuz: "))
hg = float(input("Boyunuz (Örn: 1.80): "))

index = kg / (hg**2)
zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
kilolu= (index > 24.9) and (index <= 29.9)
obez = (index > 29.9) and (index <= 34.9)

print(f"Merhaba {name}. Vücut kütle endeksiniz: {index}. Kilo durumunuz: Zayıf({zayif})")
print(f"Merhaba {name}. Vücut kütle endeksiniz: {index}. Kilo durumunuz: Normal({normal})")
print(f"Merhaba {name}. Vücut kütle endeksiniz: {index}. Kilo durumunuz: Kilolu({kilolu})")
print(f"Merhaba {name}. Vücut kütle endeksiniz: {index}. Kilo durumunuz: Obez({obez})")
"""