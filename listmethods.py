#dizi üzerinde işlem yapmak için, o nereye ait methodlar kullanılır

#.append()  => dizi içerisine eleman eklemek için kullanılır (Javascript için de geçerlidir)
#.append()  => ekleme işlemini dizinin sonuna ekleyerek gerçekleştirir. 

sehirler = [] #boş dizi
sehirler.append("ankara")
sehirler.append("edirne")
sehirler.append("istanbul")

print(sehirler[:])


#----------------------------


# .insert() => dizi içerisinde belirli bir alana veri eklemek için kullanılır 
sehirler.insert (1,"bursa") 
#1. parametrede dizinin hangi sırasına eleman eklenecek index numarası veriniz 
#2. parametre dizi içerisine eklenecek olan eleman 

print(sehirler) 



#----------------------------


# .pop => dizi içerisinden eleman silme parametre verilirse verilen index değerindeki elemanı parametre verilmezse dizinin en son elemanını siler 

print (sehirler) 
sehirler.pop(1) 
print (sehirler) 


#----------------------------

arabalar = ["mercedes", "bmw" , "range rover" , "bugatti", "aston martin", "tofaş", "karta", "serçe"]


# .remove() => dizi içerisinden eleman silmekle mükellef diğer bir methodumuzdur. pop() methodundan farkı birisi index mekanizması üzerinden silme işlemi yaparken remove() object parametre olarak işleme devam eder.

# dizi içerinde birden fazla aynı değer var ise soldan sağa ilk bulduğu elemanı siler 

# remove metodu kod metodu gibi silinen elemanı geriye teslim etmez void metottur. 

print(arabalar[:])
print(arabalar.remove("tofaş"))
print(arabalar[:])


#----------------------------

#dizi içerinde yer alan elemanları a dan z ye - 0 dan 9 a sıralayın 

print(arabalar)
arabalar.sort()
print(arabalar[:])



#----------------------------

# .reverse() => dizi içerisindeki elemanları sıralamadan tersine çevirir.

print(arabalar)
arabalar.reverse()
print(arabalar)




#----------------------------

# .len() => dizinin uzunluğunu temsil eder

print(len(arabalar))
del sehirler #sehirler dizisini tamamen silmiş olursunuz bu satır derlendikten sonra alt stırlarda arabalar dizisne ulaşamayacaksınız 

print(len(arabalar))
print(arabalar)













