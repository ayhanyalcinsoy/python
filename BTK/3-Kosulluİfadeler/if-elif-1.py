
"""
Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyerek ehliyet alabilme durumunu kontrol ediniz. Yaş en az 18,
eğitim durumu Lise ve üniversite
"""
"""
name = input ("Adınız: ")
age = int(input("Yaşınız: "))
education = input("Eğitim durumunuz: ").lower()

if (age >= 18):
    if (education == 'lise' or education == 'üniversite'):
        print(f"Merhaba {name}! Yaşınız {age} ve eğitim durumunuz {education} olduğu için ehliyet alabilirsiniz")
    else:
        print(
            f"Merhaba {name}! Yaşın {age} olmasına rağmen eğitim durumun({education}) ehliyet almak için uygun değil ")
else:
    print(f"Merhaba {name}! Yaşın({age}) ehliyet almak için uygun değil ")
"""
"""
Bir öğrencinin iki yazılı ve bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not 
bilgisini yazdırınız.
0-24 => 0
25-44 => 1
45-54 => 2
55-69 => 3
70-84 => 4
85-100 => 5
"""
"""
exam1 = float(input("Yazılı 1: "))
exam2 = float(input("Yazılı 2: "))
quiz = float(input("Sözlü: "))
ortalama = (exam1 + exam2 + quiz)/3
if (ortalama >= 0) and (ortalama <= 24):
    print (f"Not ortalamanız: {ortalama} => notunuz: 0")
elif (ortalama >=25) and (ortalama <=44):
    print(f"Not ortalamanız: {ortalama} => notunuz: 1")
elif (ortalama >=45) and (ortalama <=54):
    print(f"Not ortalamanız: {ortalama} => notunuz: 2")
elif (ortalama >=55) and (ortalama <=69):
    print(f"Not ortalamanız: {ortalama} => notunuz: 3")
elif (ortalama >=70) and (ortalama <=84):
    print(f"Not ortalamanız: {ortalama} => notunuz: 4")
elif (ortalama >=85) and (ortalama <=100):
    print(f"Not ortalamanız: {ortalama} => notunuz: 5")
else:
    print(f"Yanlış bilgi girdiniz")
"""
"""
Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
1. Bakım => 1. yıl
2. Bakım => 2. yıl
3. Bakım => 3. yıl
** süre hesabını alınan gün ay yıl bilgisine göre gün bazlı hesaplayınız
***datetime modülünü kullanmanız gerekiyor
"""
import datetime

#trafikTarihi = '2013,3,14'
tarih = input("Trafiğe çıkış tarihi (Yıl/Ay/Gün): ")
tarih = tarih.split('/')

trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = (fark.days)

if (days <= 365):
    print("1.Servis Aralığında")
elif (days >365 and days <= 365*2):
    print("2.Servis aralığında")
elif (days > 365*2 and days <= 365*3):
    print("3.Servis aralığında")
else:
    print("Hatalı bilgi girdiniz")
