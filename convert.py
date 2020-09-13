




# convert   : elinizdeki bir veri tipini farklı bir veri tipine çevirme işlemi yapar
# int ()    : tam sayı veri tipine çevirir
# str()     : string (metinsel) değere çevirme işlemi yapar
# float()   : ondalıklı değere çevirme işlemi yapar
# chr()     : verdiğiniz ssayısal değerin, karaker karşılığıni temsil eder
# odr()     : verdiğiniz karakterin, ascil (sayısal) karşılığıni temsil eder


sayi1 = input("Lütfen 1. sayısı giriniz : ")
sayi2 = input("Lütfen 2. sayıyı giriniz : ")
print(sayi1)
print(type(sayi1))

print (sayi1 + sayi2)
# ctrl + k + c => yorum satırına alır 
# ctrl + k + u => yorum satırından alır 
# alt + shift + f => kodları düzenler 
# alt + shift + f => kodları düzenler 

toplam = float(sayi1) + float(sayi2) 
print (toplam) 
result = int(sayi1) + int(sayi2) 
print (result) 

print(chr(65), ord('A'))
print(chr(90), ord('Z'))
print(chr(97), ord('a'))
print(chr(122), ord('z'))

sayi = 100

print("sayinin degeri" + sayi) 

