# try:
#     sayi_bir = int(input("Lütfen 1. sayıyı giriniz: "))
#     sayi_iki = int(input("Lütfen 2. sayıyı giriniz : "))

#     toplam =sayi_bir + sayi_iki 
#     fark = sayi_bir - sayi_iki
#     carpim = sayi_bir * sayi_iki
#     bolum = sayi_bir / sayi_iki
#     mod = sayi_bir % sayi_iki 


#     print(f"Sayıların Toplamı: {toplam} \nSayıların Farkı : {fark} \nSayıların Bölüm : {bolum} \nSayıların Çarpımı : {carpim}")

# except ValueError:
#      print("ValueError")

# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except FileExistsError:
#     print("FileDivisionError")
# except:
#     print("Tüm hataları kabul ediyorum, özür dilerim")




try:
    sayi = int(input("Lütfen sadece sayısal değer giriniz: "))
    print("gelen sayı : ", sayi)
    sayi=sayi / 0 
    print ("İşlem sonucu") 
except ValueError as ex:
    print("Lütfen Tekrar deneyiniz")
    print("Sistem mesajı: " , ex )
except Exception as ex:
    print("işlem hatası")
    print("Sistem mesajı : ")
