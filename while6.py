sayilar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# dizi içerisinde yer alan, tek sayıları bir diziye çift sayıları ayrı bir diziye ekleyiniz. İşlem sonunda toplam dizi içerisinde kaç eleman var kullanıcıya bildirim veriniz.

# Tek sayıların adedi : 

i = 0 
tek_sayilar = []
cift_sayilar = []

while i < len(sayilar) :
    if i % 2 == 0:
        cift_sayilar.append(sayilar[i])
    else:
        tek_sayilar.append(sayilar[i])
    i += 1 

print ( f"Tek sayıların toplamı :{len(tek_sayilar)}\nÇift sayıların toplamı:{len(cift_sayilar)}" )
print (f"Tek sayılar : {tek_sayilar}\nÇift sayılar : {cift_sayilar}")

# Dışardan girilen metin içerisinde yer alan sesli ve sessiz harfleri ayrıştırınız ve kullanıcıya toplam adetleirni gösteriniz.



metin = input("Lütfen bir metin giriniz: ")

i = 0 
toplamsesli = []
sesli = ["a","e","ı","i","o","ö","u","ü"]
toplamsessiz = [] 

while i < len(metin) :
    if metin[i] in sesli:
        toplamsesli.append(metin[i])
    else:
        toplamsessiz.append(metin[i])
    i += 1

print (f"Sessiz haflerin toplamı : {len(toplamsessiz)}\nSesli hatflerin toplamı: {len(toplamsesli)}")






