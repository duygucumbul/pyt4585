

# .startswith() => metnin parametredeki değer ile başlayıp başlamadığını (True ya da False ) olarak teslim eder

metin = "bilge adam beşiktaş"
result = metin.startswith("bil")

print(result) 

print(f"parametrede gönderdiğiniz değer \"bil\" anahtar kelimesi ile başlama{'' if result else 'ma'}ktadır")
#True
# parametrede gönderdiğiniz değer "bil" anahtar kelimesi ile başlamaktadır
