# .capitalize() => parametrede verilen değerin ilk harfin büüyk olarak değiştirir 

isim = "murat vuranok"
print(isim.capitalize()) # Murat vuranok



# .title() => parametredeki değerin her bir kelimenin ilk harfini büyük olarak temsil eder
print(isim.title()) # Murat Vuranok 


# .sorted() => dizi içerisinde yer alan elemanları A'dan Z'ye 0 dan 9 a sıralama yapar 
dizi = ['a','s', 'd', 'f', 'g', 'h','l','ş','ç','ğ','i']
#['a', 'd', 'f', 'g', 'h', 'i', 'l', 's', 'ç', 'ğ', 'ş']


print(sorted(dizi))


print(sorted('bilgeadambeşiktaş'))
#['a', 'a', 'a', 'b', 'b', 'd', 'e', 'e', 'g', 'i', 'i', 'k', 'l', 'm', 't', 'ş', 'ş']


import locale 
# locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254") # windows için
locale.setlocale(locale.LC_ALL,"tr_TR") # GNU\Linux için 

sonuc = sorted("bilgeadam", key = locale.strxfrm)
print(sonuc) 
#['a', 'a', 'b', 'd', 'e', 'g', 'i', 'l', 'm']