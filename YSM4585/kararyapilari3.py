#kullanıcı dışardan girdiğin sayının tek veya çift olma durumunu kontrol etme, sayi tek ise, sayı tektir uyarısı çift ise, sayı çifttir uyarısı veriniz. 

try: 
    sayi = int(input("Lütfen sayi giriniz: "))
    if (sayi % 2 == 0) :
         print ("sayi çifttir")
    else :
        print("sayi tektir")
except Exception as mahmud:
    print(mahmud) 
    print ("Sayısal değer giriniz")

