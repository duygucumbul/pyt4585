#karar yapıları
#Karşılaştırma operatorleri 

# == (eşit eşittir) soldaki değerin, sağdaki değere eşit olma durumu
# 1 == 1 => true  - if
# 1 == 2 => false - else 

# != (eşit değildir) soldaki değerin sağdaki değere eşit olmama durumu
# 1 != 1 => false - else
# 1 != 2 => true  - if

# > (soldaki değerin sağdaki değerden büyük olma durumu)
# 2 > 1 => true  - if
# 1 > 1 => false - else 

# < (soldaki değerin sağdaki derğerden küük olma durumu)
# 1 < 2 => true  - if
# 2 < 1 => false - else 

# >= ( soldaki değerin sağdaki değerden büyük veya eşit olma durumu)
# 1 >= 1 => true - eşit oma - if
# 2 >= 1 => true - büyük olma - if
# 1 >= 2 => false - else 

# <= (soldaki değeri sağdaki değerden küçük ve ya eşit olma durumu)
# 1 <= 1 => true - eşit olma  - if
# 1 <= 5 => true - küçük olma - if
# 5 <= 1 => false - else 


username= input("Lütfen kullanıcı adınızı giriniz: ")
username= username.lower()\
    .replace("ı","i")\
    .replace("ç","c")\
    .replace ("ş","s")\
        .replace("ö","o")\
            .replace("ğ","g")\
                .replace("ü","u")


print(username) 

if(username== "admin"):
    print("tebrikler, giriş yaptınız")
else:
    print("Kullanıcı adınız yanlış")
    