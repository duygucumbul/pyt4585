

# .center()   => prametrede verdiğiniz sayısal değeri metnin sağına ve soluna eşit olarak dağıtır (küsürat dahil değildir) 
# boşluk ekleme işlemi yaparken metnin uzunluğu parametrede verilen değerden çıkartılır kalan sonuc sola ve sağa dağıtılır 

metin = "bilge adam"
print(len(metin)) #10

metin = metin.center(20)
print(len(metin))  #20
print("metin başı", metin, "metin sonu") # metni ortalıyoruz verdiğiniz değere göre (20) 
#metin başı      bilge adam      metin sonu
