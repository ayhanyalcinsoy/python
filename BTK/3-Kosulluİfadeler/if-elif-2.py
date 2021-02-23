#Girilen bir sayının 0-100 arasında olup olmadığını kontrol et
"""
sayi = float(input("Bir sayı giriniz: "))
if (sayi>0) and (sayi<=100):
    print (f"Girdiniz {sayi} sayısı, 0-100 arasındadır")
else:
    print(f"Girdiniz {sayi} sayısı, 0-100 arasında değildir")
#Girilen bir sayının pozitif çift sayı olup olmadığını kontrol et
if (sayi>=0):
    if (sayi%2==0):
        print(f"Girdiğiniz sayı pozitif çift sayıdır")
    else:
        print(f"Girdiğiniz sayı pozitif tek sayıdır")
else:
    if(sayi <= 0):
        if (sayi % 2 == 0):
            print(f"Girdiğiniz sayı negatif çift sayıdır")
        else:
            print(f"Girdiğiniz sayı negatif tek sayıdır")
"""

# email ve parola bilgileri ile giriş kontrolü
"""
email = "email@pisilinux.org"
passw = "abc123"

yourEmail = input("E-posta adresini giriniz: ")
yourPassw = input("Parolanızı giriniz: ")

if(yourEmail == email):
    if(yourPassw == passw):
        print ("Başarılı bir giriş yaptınız")
    else:
        print("Parolanız yanlış.")
else:
    print("E-posta adresiniz yanlış")
"""

# Girilen 3 sayının büyüklük olarak karşılaştırılması
"""
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a>b) and (a>c):
    print(f"{a} sayısı {b} ve {c} sayılarından büyüktür")
elif(b>a) and (b>c):
    print (f"{b} sayısı {a} ve {c} sayılarından büyüktür")
else:
    print (f"{c} sayısı {a} ve {b} sayılarından büyüktür")
"""

"""
Kullanıcıdan 2 vize (%60) ve bir final notu
     50 ve üzeri ise geçti değilse kaldı.
     Ortalama 50 bile olsa finalden enaz 50 almalı
     Finalden 70 aldığında ortalamanın önemi olmasın
"""
"""
vize1 = float(input("Vize1: "))
vize2 = float(input("Vize2: "))
final = float(input("Final: "))

ortalama = (((vize1+vize1)/2)*0.6) + (final*0.4)

if(ortalama >= 50):
    if (final >= 50):
        print(f"Not ortalamanız {ortalama} ve dersten geçtiniz")
    else:
        print(f"Not ortalamanız {ortalama} ancak dersten geçmek için finalden en az 50 almanız gerekir")
else:
    if (final>=70):
        print("Finalden 70 aldığınız için dersten geçtiniz")
    else:
        print(f"Not ortalamanız {ortalama} olduğu için dersten başarısız oldunuz.")

"""
"""
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
if (index >= 0) and (index <= 18.4):
    print(f"Merhaba {name}. Vücut kütle endeksiniz: {index}. Kilo durumunuz: Zayıf)")
elif (index > 18.4) and (index <= 24.9):
    print(f"Merhaba {name}. Vücut kütle endeksiniz: {index}. Kilo durumunuz: Normal)")
elif (index > 24.9) and (index <= 29.9):
    print(f"Merhaba {name}. Vücut kütle endeksiniz: {index}. Kilo durumunuz: Kilolu)")
elif (index > 29.9) and (index <= 35.9):
    print(f"Merhaba {name}. Vücut kütle endeksiniz: {index}. Kilo durumunuz: Obez)")
else:
    print ("Hatalı bilgi girdiniz")