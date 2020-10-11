

# .endswith() => metninizin parametrede gönderdiğiniz değer ile bitip bitmediğini kontrol eder 

metin = "bilge adam beşiktaş python dersleri"
sonuc = metin.endswith("eri")

if sonuc :
    print("parametrede gönderdiğiniz değer eri kelimesi ile bitmekte")
else:
    print("parametrede gönderdiğiniz değer eri kelimesi ile bitmemekte")




# ternary if kullanarak tek satırda mesaj veriniz 

print(
    f"parametrede gönderdiğiniz metinde eri yer alma{ '' if sonuc else 'ma' }ktadır")