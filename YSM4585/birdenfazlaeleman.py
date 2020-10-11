# birden fazla elemanla çalışıcak ise, tek tek değişken tanımlamak yerine dizi kullanıyoruz
# tanımlama şekli
sehirler = ("istanbul", "konya", "edirne", "rise",
            "ankara", "eskişehir", "adana", "kayseri")

# bir dizinin max index değeri o dizinin eleman sayısı (uzunluğu) 1- değeridir
# 1 2 3 4 5 6 7 8 => eleman sayısı
# 0 1 2 3 4 5 6 7 => o elemanın dizi içindeki index değeri

# eleman sayısı => dizi içerisindeki toplam adet
# index değeri => dizi içinde yer alan herhangi bir elemana ulaşma şekli


print(sehirler[0])  # diiznin ilk elemanını ekrana yazdırdı


index = len(sehirler)  # toplam eleman sayısını teslim eder
index = len(sehirler) - 1  # o dizinin max index değerini teslim eder

print(sehirler[index])

print(sehirler[2:7])
# 1. parametrede verilen index değeri (dahil) nerden başlayacağım
# 2. parametrede verilen index değerininn bir alt değerine kadar olan elemanları listeler


# dizinin tüm elemanlarını ekrana yazdırmak istersek
print(sehirler[:])


# adana parametresi  dizi içerisinde geçmekte midir, geçmemekte midir
print("adana" in sehirler)
# kullanıcı dışardan şehir adı girecek var ise bu şehir dizi içerisinde yer almaktadır yok ise bu dizi şehir içerisinde yer almamaktadır mesajını verinir.


sehir_adi = input("Lütfen bir şehir adı giriniz: ")
mesaj = ""

if sehir_adi in sehirler:
    mesaj = f"parametredeki {sehir_adi} sehri, dizi içindedir"
else:
    mesaj = f"{sehir_adi} şehri, şehirler dizisinin içinde değil"
print(mesaj)

result = f"parametredeki {sehir_adi} dizi içerisindedir" if sehir_adi in sehirler else f"parametredeki {sehir_adi} dizi içinde yer almamaktadır"
print(result)

# ternary opt.
# kosul içinde true dönerse soldaki alan false dönerse sağdaki alan çalışır


print(
    f"parametreki {sehir_adi} , dizide yer alma{'' if sehir_adi in sehirler else 'ma' }ktadır")

print("parametreki {sehir_adi} , dizide yer alma{}ktadır".format(
    sehir_adi, ("" if sehir_adi in sehirler else "ma")))


myList1 = ["şehirler dizisi"]
print(myList1)

myList2 = ["arabalar dizisi"]
print(myList2)

myList3 = ["renkler dizisi"]
print(myList3)

result = list(zip[myList1, myList2, myList3])
print(result)
