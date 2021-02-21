username = 'ayhanyalcinsoy'
passw = "abc123"

userName = input("Kullanıcı adını giriniz: ")
passW = input("Parolanızı giriniz: ")

if userName == username:
    if passW == passw:
        print ("Hoşgeldiniz")
    else:
        print("Parolanız yanlış")
else:
    print ("Kullanıcı adınız yanlış")