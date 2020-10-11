# Örnek : Dışardan girilen kelimenin uzunluğu, 8 karaktere eşit veya uzunsa, parola onaylandı, kısa ise, daha uzun bir şifre seçiniz uyarısı veriniz.


parola = input("Lütfen parola giriniz: ") 
if len(parola) < 8:
    print("Daha uzun bir parola giriniz")
else:
    print ("Parola onaylandı")