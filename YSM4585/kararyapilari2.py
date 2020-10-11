# kullanıcı dışardan net değerini girecek ve girilen not 0'dan küçükse, 0'dan küçük not giemezsiniz uyarısı, 100'den büyükse 100'den büyük not 
# girişi apamazsınız uyarısı, girilen no 0'a veya 100'e eşit ve küçükse, kullanıcıya girdiği notu gösteriniz.


try: 
    not_ = int(input("Lütfen notunuzu giriniz: "))
    if not_ < 0 :
         print("0'dan küçük bir değer giremezsiniz")
    elif not_ > 100:
        print ("100'den büyük değer giremezsiniz")
    else:
        print("Notunuz : ", not_) 

except :
    print("SAdece not gireceksin, ne kadar zor olabilir?")
