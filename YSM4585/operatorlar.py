# Aritmetik operaratorler
# +, -, /, *, %,**

sayi1 = 120
sayi2 = 50
toplam = sayi1 + sayi2
print("İşlem Sonucu" + " "*50 + str(toplam))

# dışarıdan girilen 2 sayının 4 işlemi

sayi3 = 56
sayi4 = 78
toplam = sayi3 + sayi4
print("işlem sonucu2" + " "*10 + str(toplam))

cikarma = sayi4 - sayi3
print("işlem sonucu3" + " "*10, str(cikarma))

bolme = sayi3 / sayi4
print("İşlem sonucu4", " "*10, str(bolme))

carpma = sayi3 * sayi4
print("işlem sonucu5", " "*10, str(carpma))


sayi1 = float(input("Lütfen 1. sayıyı giriniz :"))
sayi2 = float(input("Lütfen 2. sayıyı giriniz: "))

toplam = sayi1 + sayi2
fark = sayi1 - sayi2
bolum = sayi1 / sayi2
mod = sayi1 % sayi2
carpim = sayi1 * sayi2
kuvvet = sayi1 ** sayi2

result = "Toplama işlemi sonucu: " + \
    str(toplam) + "\n Çıkarma işlemi sonucu : " + \
        str(fark) + "\nBölme işlemi sonucu : " + str(bolum) + "\nMod İşlemi Sonucu : " + \
            str(mod) + "\nKuvvet Alma İşlemi Sonucu : " + \
                str(kuvvet) + "\nÇarpma işemi Sonucu : " + str(carpim)


print(result)
