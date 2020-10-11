# dışardan gelicek olan parametre sayısı belirsiz olan durumlar için kullanılan metot tekniği ?

def Hesapla(*sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    return toplam 


result = Hesapla(1,2,3,4,5,6,7,8,9)
print("toplama işleminin sonucu:", result)

# parantezn içindeki * birden fazla veri girilebilmeyi sağlıyor 
