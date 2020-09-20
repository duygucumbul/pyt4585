#Örnek: Dışarıdan kullanıcı not girişi sağlayacak
# 0 - 30 => FF
# 31 - 50 => DD
# 51 - 70 => CC
# 71 - 84 => BB
# 85 -100 => AA harf notunu aldınız uyarısı veriniz.

try: 
    not_ = int(input("Lütfen notunuzu giriniz: "))
    result = "Girilen {} notun karşılık harf notu: {}" 
    if not_ <= 30 and not_ >= 0 :
        result = (result.format(not_,"FF")) 
    elif not_ >= 31 and not_<= 50 :
        result = (result.format(not_,"DD"))
    elif not_ >= 51 and not_ <=70 :
        result = (result.format(not_,"CC"))
    elif not_ >= 71 and not_ <= 84 :
        result = (result.format(not_,"BB"))
    elif not_ >= 85 and not_ <= 100 :
        result = (result.format(not_,"AA"))
    else:
        result = ("0 ile 100 arasında bir değer giriniz")

    print (result) 
except ValueError as mahmud :
    print (mahmud) 



# try: 
#     not_ = int(input("Lütfen notunuzu giriniz: "))
#     result = "Girilen {} notun karşılık harf notu: {}" 
#     if  not_ <= 100 and not_ >= 0 :
#         result = "harf notunuz: "
#     if not_ <= 30 :
#         result = (result.format(not_,"FF")) 
#     elif not_<= 50 :
#         result = (result.format(not_,"DD"))
#     elif  not_ <=70 :
#         result = (result.format(not_,"CC"))
#     elif  not_ <= 84 :
#         result = (result.format(not_,"BB"))
#     elif not_ <= 100 :
#         result = (result.format(not_,"AA"))
#     else:
#         result = ("0 ile 100 arasında bir değer giriniz")

#     print (result) 
# except ValueError as mahmud :
#     print (mahmud) 