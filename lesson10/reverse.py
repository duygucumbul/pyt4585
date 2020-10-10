# .reverse() =>dizide var olan elemanları sıralama yapmadan tersine çevirir 

sayilar = [1,2,3,4,5,6,7,8,9]
karakterler = ['a','b','c','d','e','f']

sayilar.reverse()
karakterler.reverse()
print(sayilar)
print(karakterler)


#------------------------------------------------------------

# içerisinde verilen parametreye göre soldan sağa doğru ayırma işlemi yapar 

elemanlar = 'yazılım,sistem,ofis,muhasebe,teknik çizim, web grafik'
elemanlar = elemanlar.split(',')
print(elemanlar)
#['yazılım', 'sistem', 'ofis', 'muhasebe', 'teknik çizim', ' web grafik']

elemanlar = 'yazılım,sistem,ofis,muhasebe,teknik çizim, web grafik'
elemanlar = elemanlar.split()
print(elemanlar)
#['yazılım,sistem,ofis,muhasebe,teknik', 'çizim,', 'web', 'grafik']

#------------------------------------------------------------

metin = "murat vuranok yazılım beşiktaş istanbul"

sonuc = metin.split(" ",3) 
# birinci parametrede verdiğiniz seperator değerine göre, 2. paarmetrede verdğiniz adet ayırma işlemi yapacaktır 
print(sonuc) 
# ['murat', 'vuranok', 'yazılım', 'beşiktaş istanbul']
