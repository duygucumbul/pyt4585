# kullanıcı dışardan ürün adı girecek,
# domates - biber - patlıcan => sebze reyonu
# şampuan - parfüm - deodorant => kozmetik reyonu
# cep telefonu - televizyon - bilgisayar - kulaklık => teknoloji reyonu

# farklı bir ürün girerse, bu ürün bizde bulunmamaktadır uyarısı veriniz.

urun = input("Lütfen ürün adı giriniz: ").lower().replace(" ","") 

if urun == "domates" or urun == "biber" or urun == "patlican":
    print("Sebze reyonu")
elif urun == "sapuan" or urun == "parfum" or urun == "deodorant":
    print("Kozmetik reyonu")
elif urun == "cep telefonu" or urun == "televizyon" or urun == "bilgisayar" or urun == "kulaklık":
    print("Teknoloji reyonu")
else:
    print("Bu ürün bizde bulunmamaktadır")


urun = input("Lütfen ürün adı giriniz: ").lower().replace(" ","") 

if len(urun) > 1: 
    result = "Aradığınız {}, {} reyonundadır"
    if urun == "domates" or urun == "biber" or urun == "patlican":
        result = result.format(urun, "Sebze")
    elif urun == "sapuan" or urun == "parfum" or urun == "deodorant":
        result = result.format(urun, "Kozmetik")
    elif urun == "cep telefonu" or urun == "televizyon" or urun == "bilgisayar" or urun == "kulaklık":
        result = result.format(urun, "Teknoloji")
    else:
        result ("Bu ürün bizde bulunmamaktadır")
    print (result) 
else: 
    ("Lütfen bir ürün adı giriniz")

