website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz(40 saat)"

#course kararkter dizisinde kaç karakter bulunmaktadır.
charCount = len(course)
print (charCount)

#website içideki 'www' karakterlerini alın
charChoose = website[7:10]
print (charChoose)

#website içinden 'com' karakterini alın
lenght = len(website)
charChoose1 = website[lenght-3:lenght]
print (charChoose1)

#course içinden ilk 15 ve son 15 karakteri alın
firstLast = course[:15] + course[charCount-15:]
print (firstLast)

#course ifadesindeki karakterleri tersten yazdırın
ters = course[::-1]
print (ters)

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"
#verilen değişkenleri  şu şekilde yazdırın: Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis
print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")

#Hellow world ifadesindeki w karakterini W ile değiştirin
hello = "Hello world"
newHello = hello[0:5] + ' W' + hello[-4:]
print (newHello)

#abc ifadesinin yan yana 3 tane yazdırın
x = "abc"
print (x*3)
