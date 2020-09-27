#kullanıcının dışarıdan girdiği sayıları toplamını ekrana yazdırınız 
#örenk => 123 => 6 

sayilar = input("Lütfen sayilar giriniz: " )

sayilar_toplami = 0

index = 0
a= int(sayilar [index])

while index < len(sayilar) :
    sayilar_toplami += int(sayilar[index])
    index += 1  #girdiğin sayıyı tut ve bir ekle anlamına geliyor 
print ("Girilen sayilar_toplami : {}".format(sayilar_toplami))

    

    
