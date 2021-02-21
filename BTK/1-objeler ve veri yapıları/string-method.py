message = "Hello There. My name is Sadık Turan"

message = message.upper()  #Tümü büyük harf
print(message)
message = message.lower()  #Tümü küçük harf
print(message)
message = message.title()  #Her kelimenin ilk harfi büyük
print(message)
message = message.capitalize()  #Mesajın ilk karakteri büyük
print(message)
message = message.strip()  # başta ve sonda bulunan boşluk karekterlerini siler
print(message)
message = message.split()  # boşluk karekterlerinden mesajı böler
print(message[0])  #bölünen mesajın ilk parçasını yazdırır
message = ' '.join(
    message)  #bölünen mesajı boşluk karakteri ekleyerek birleştirir.
print(message)
index = message.find("Hello")
print(index)

isFound = message.startswith('H')
print(isFound)

isFound = message.endswith('n')
print(isFound)

message = message.replace('sadik', 'Çınar')
print(message)

message = message.replace('i', 'ı').replace('Ç', 'C').replace('t', 'T')
print(message)
