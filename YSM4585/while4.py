# 1 ile 1000 (dahil) arasındaki tek sayılar ile çift sayıların toplam adedini ekrana yazdırınız 

index = 1
tek_sayilar_toplami = 0
cift_sayilar_toplami = 0

while index <= 1000:
    if index % 2 == 0:
        cift_sayilar_toplami = cift_sayilar_toplami + 1 
    else :
        tek_sayilar_toplami +=1 
    index += 1

print(f"Tek sayıların toplam adedi :{tek_sayilar_toplami}\nÇift Sayıların toplamı: {cift_sayilar_toplami}")


# Kullanıcının panel üzerinden girdiği metni alt alta yazdırınız.

# import os 
# clear = os.system ('clear')
# clear()

metin = input("Lütfen bir metin giriniz: ")
index = 0
while index < len(metin) :
    print(metin [index])
    index += 1 




