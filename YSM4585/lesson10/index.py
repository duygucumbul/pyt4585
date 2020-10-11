

# .index() , .rindex()

metin = "bilge adam beşiktaş şubesi"


# parametrede verdiğiniz değerin metin içinde yer alan index değerini teslim eder, metin içerisinde aynı karakter birden fazla içeriyorsa 
# ilk bulduğu değerin index numarasını eğer parametrede gönderdiğiniz değer metin içinde geçmiyorsa size Valueerror : substing not found değerini teslim eder 

result = metin.index("a")
print(result)
#6

sonuc = metin.rindex("a")
print(sonuc)
#17

# metin içinde parametrede gönderilen değerin birden fazla olup olmadığını kullanıcıya mesaj olarak dönen bir metot yazınız 
# metot içeriye metin veya paarmetre alacak geriye str mesaj gönderecek 

def metot(metin,parametre):             # var mı yok mu diye sorguluyoruz 
    if (metin.index(parametre) == metin.rindex(parametre)):
        return f"parametredeki {parametre} değerin, {metin} içinde 1 defa vardır"
    elif (metin.index(parametre) != metin.rindex(parametre)):
        return f"parametredeki {parametre} değerin, {metin} içinde 1 den fazla vardır"
    else:
        return f"parametredeki {parametre} değerin, {metin} içinde yoktur"



metin = input("Lütfen bir metin giriniz:")
result = metot(f"{metin}","a")
print(result)




