website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz(40 saat)"

# ' Hellow World ' baş ve sondaki boşlukları silin
greeting = ' Hellow World '.strip()
print (greeting)
# 'www.sadikturan.com' dan sadikturan dışındakileri sil
adres = 'www.sadikturan.com'.strip('w.com')
print(adres)
# course bütün karakterleri küçük harf yazdır
course = course.lower()
print(course)
#website içinde kaç tana 'a' var
print (website.count('a'))
#website www ile başlayıp com ile bitiyor mu
isFound = website.startswith('www')
print(isFound)
isFound = website.endswith('com')
print(isFound)
#website içinde com var mı
print (website.find('com'))
# course içindeki harfler alfabetik mi (isalpha, isdigit)
print(course.isalpha())
print(course.isdigit())
#'Contents' ifadesini 50 karakter içinde sağda ve solda * içine yaz
contents = 'Contents'.center(50, '*')
print(contents)
# course dizinindeki boşlukları - ile değiştir
course = course.replace(' ', '-')
print (course)
#'hello world' içindeki world ü there ile değiştir.
greeting = 'Hellow World'.replace('World', 'There')
print (greeting)
#course dizisini - karakterlerinden ayırın
course = course.split('-')
print (course)
