



def metot(**param) :
    print("-"*25)
    for key, value in param.items():
        print("{:8} : {}".format(key,value))
    print("-"*45)


metot(
    Ad = "duygu",
    Soyad = "cumbul",
    telefon = "34567890",
    Mail = "sdfghjk"
)

ad = input("Lütfen adınızı giriniz: ")
lastname = input("Lütfen soyadınızı giriniz:")
metot(Ad=ad, Soyad = lastname)