

# .find() , rfind() => aradığınız elemanın index değerini teslim eder eğer dizi veya metin içerisindeki değer birden fazlaysa find() ilk buldığu elemanı 
# rfind() son bulduğu elemanı teslim eder dizi içerisinde eğer aradığınız eleman yok ise size -1 değerini teslim eder 

# index metot ile çalışma presibi aynıdır fark => index valueerror verirken find metotu -1 değeri teslim eder parametredeki elemanı içermiyorsa

metin = "bilge adam beşiktaş şubesi"

result = metin.index("a")
print(result)
#6

sonuc = metin.rindex("a")
print(sonuc)
#17

sonuc = metin.find("x")
print(sonuc)
#-1

sonuc = metin.rfind("x")
print(sonuc)
#-1 
