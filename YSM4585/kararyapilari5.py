

# mantıksal operatorler

# and sorguya katılan her bir koşulun sağlanması durumu
# or sorguya katılan herhangi bir koşulun sağlanması durumu
# not sorguya olumsuzluk katar, değil ise

# username = input("Lütfen kullanıcı adınızı giriniz: ")
# if (username == "admin") :
#     password = input("Lütfen şifrenizi giriniz: ")
#     if password == "123456":
#         print ( "Giriş yaptınız")
#     else:
#         print("Şİfreniz hatalı, kontrol ediniz")

# else:
#     print ("Kullanıcı adınız hatalı, kontrol ediniz")


# username= input ("Lütfen kullanıcı adınızı giriniz: ")
# password = input ("Kullanıcı şifrenizi giriniz: ")

# if username == "admin" and password == "123456":
#     print ("Tebrikler giriş yaptınz")
# else:
#     print ("Kullanıcı bilgilerinizi kontrol ediniz")


# Örnek: Dışarıdan kullanıcı not girişi sağlayacak
# 0 - 30 => FF
# 31 - 50 => DD
# 51 - 70 => CC
# 71 - 84 => BB
# 85 -100 => AA harf notunu aldınız uyarısı veriniz.

# try: 
#     not_ = int(input("Lütfen notunuzu giriniz: "))
#     result = "Girilen {} notun karşılık harf notu: {}" 
#     if not_ <= 30 and not_ >= 0 :
#         result = (result.format(not_,"FF")) 
#     elif not_ >= 31 and not_<= 50 :
#         result = (result.format(not_,"DD"))
#     elif not_ >= 51 and not_ <=70 :
#         result = (result.format(not_,"CC"))
#     elif not_ >= 71 and not_ <= 84 :
#         result = (result.format(not_,"BB"))
#     elif not_ >= 85 and not_ <= 100 :
#         result = (result.format(not_,"AA"))
#     else:
#         result = ("0 ile 100 arasında bir değer giriniz")

#     print (result) 
# except ValueError as mahmud :
#     print (mahmud) 



# try: 
#     not_ = int(input("Lütfen notunuzu giriniz: "))
#     result = "Girilen {} notun karşılık harf notu: {}" 
#     if  not_ <= 100 and not_ >= 0 :
#         result = "harf notunuz: "
#     if not_ <= 30 
#         result = (result.format(not_,"FF")) 
#     elif not_<= 50 :
#         result = (result.format(not_,"DD"))
#     elif  not_ <=70 :
#         result = (result.format(not_,"CC"))
#     elif  not_ <= 84 :
#         result = (result.format(not_,"BB"))
#     elif not_ <= 100 :
#         result = (result.format(not_,"AA"))
#     else:
#         result = ("0 ile 100 arasında bir değer giriniz")

#     print (result) 
# except ValueError as mahmud :
#     print (mahmud) 
  
  


# ---

# kullanıcı dışardan ürün adı girecek,
# domates - biber - patlıcan => sebze reyonu
# şampuan - parfüm - deodorant => kozmetik reyonu
# cep telefonu - televizyon - bilgisayar - kulaklık => teknoloji reyonu

# farklı bir ürün girerse, bu ürün bizde bulunmamaktadır uyarısı veriniz.

# urun = input("Lütfen ürün adı giriniz: ").lower().replace(" ","") 

# if urun == "domates" or urun == "biber" or urun == "patlican":
#     print("Sebze reyonu")
# elif urun == "sapuan" or urun == "parfum" or urun == "deodorant":
#     print("Kozmetik reyonu")
# elif urun == "cep telefonu" or urun == "televizyon" or urun == "bilgisayar" or urun == "kulaklık":
#     print("Teknoloji reyonu")
# else:
#     print("Bu ürün bizde bulunmamaktadır")


# urun = input("Lütfen ürün adı giriniz: ").lower().replace(" ","") 

# if len(urun) > 1: 
#     result = "Aradığınız {}, {} reyonundadır"
#     if urun == "domates" or urun == "biber" or urun == "patlican":
#         result = result.format(urun, "Sebze")
#     elif urun == "sapuan" or urun == "parfum" or urun == "deodorant":
#         result = result.format(urun, "Kozmetik")
#     elif urun == "cep telefonu" or urun == "televizyon" or urun == "bilgisayar" or urun == "kulaklık":
#         result = result.format(urun, "Teknoloji")
#     else:
#         result ("Bu ürün bizde bulunmamaktadır")
#     print (result) 
# else: 
#     ("Lütfen bir ürün adı giriniz")



# ---

# kullanıcı dışardan sipariş alınacak kitap adedi girilecek,
# siPARİŞ sayısı : 0 veya altı is uyarı veriniz
# siapriş sayısı : 1 ile 20 ise % 5 indirm uygulayınız
# sipariş sayısı : 21 ile 50 ise % 10
# sipariş sayısı : 51 - 80 ise %15
# siapriş sayısı : 81 - 100 ise %20
# sipariş sayısı : 100 den büyük ise %25


try :
    #pass 
    adet = int(input("Lütfen kitap adedi yazınız: "))
    biirm_fiyat = 5 
    total = 0 
    discount = ""
    
    result = """
    verilen sipariş adedi :   {}
    adet birim fiyatı : {} 
    toplam tutar : {}
    yapılan indiirm oranı : {}
    toplam ödemeniz gereken tutar: {}
    """
    if adet > 0:
        if adet <= 20:
            discount = "%5"
            total = (biirm_fiyat * adet) * 0.95
        elif adet <= 50:
            discount = "%10"
            total = (biirm_fiyat * adet) * 0.90
        elif adet <=80:
            discount = "%15"
            total = (biirm_fiyat * adet) * 0.85
        elif adet <= 100 :
            discount = "%20" 
            total = (biirm_fiyat * adet) * 0.80
        else:
            discount = "%25" 
            total = (biirm_fiyat * adet) * 0.75
        print (result.format(adet, biirm_fiyat, (adet * biirm_fiyat), discount, total))

    else :
        print ("Minimum sipariş adedi 1'dir") 
except Exception as mahmud :
    pass 




