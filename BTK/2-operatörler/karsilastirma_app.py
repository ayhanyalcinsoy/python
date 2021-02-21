# Girilen iki sayıdan hangisi büyüktür

a = int(input("a: "))
b = int(input("b: "))
isBuyuk = (a>b)
print (f"a:{a} sayısı b:{b} sayısından büyüktür {isBuyuk}")

#Kullanıcıdan 2 vize (%60) ve bir final (%40) notu al ve ortalmayı hesapla

vize1 = float(input("Vize1 : "))
vize2 = float(input("Vize 2: "))
final = float(input("Final: "))
ortalama = (((vize1 + vize2)/2)*0.6) + (final*0.4)
print(f"Not ortalamanız {ortalama} ve dersten geçme durumunuz : {(ortalama>=50)}")

#Girilen bir sayının tek mi çift mi olduğunu yazınız

sayi = int(input("Sayı: "))
ciftmi = (sayi % 2 == 0)
print (f"Girdiğiniz sayının çift olma durumu: {ciftmi}")

#Girilen bir sayının negatif mi pozitif mi olduğunu yazınız

c = int(input("Bir sayı giriniz: "))
pozitifmi = (c > 0)
print (f"Girdiğiniz {c} sayısı pozitiftir: {pozitifmi}")

# Parola ve email bilgisi isteyip doğruluğunu kontrol edin (email@sadikturan.com pass: abc123)
email = 'email@sadikturan.com'
passw = 'abc123'

yourEmail = input("E-posta adresinizi giriniz: ")
yourPassw = input("Parolanızı giriniz: ")
isEmail = (yourEmail == email.strip().lower())
isPassw = (yourPassw == passw.strip().lower())

print(f"Girmiş olduğunuz e-posta adresi: {isEmail}\nGirmiş olduğunuz parola: {isPassw}")