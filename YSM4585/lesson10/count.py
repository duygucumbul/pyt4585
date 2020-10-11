

# .count() => parametredeki değerin metin içinde kaç adet olduğunu teslim eder 

metin = "bilge adam beşiktaş"

sonuc= metin.count('b')
print (f"parametredeki değer, metindeki {sonuc} kadar geçmektedir")  
# sonuc = 2 




sehirler = ["amkara", "edirne", "eskisehir", "urfa", "adana", "eskisehir", "bursa"]
param = "eskisehir"
result = sehirler.count(param) 
print(f"{param} anahtar kelimesi dizi içinde toplam {result} tanedir")
#eskisehir anahtar kelimesi dizi içinde toplam 2 tanedir



metin = "murat vuranok"

retVal = metin.count("u")
print (retVal) 
#2
retVal = metin.count("u", 2)
print (retVal)
#1


retVal = metin.count("u", 2, len(metin))
retVal = metin.count("u", 2, 7)         # metnin ilk iki harfine bakmadan 7 adım giderek u var mı yok mu diye sorgulamak , "mu" fix bi başlangıç olabilir - htpp gibi 
print (retVal)                          # belirtmek gerekiyor aralığı 
#1