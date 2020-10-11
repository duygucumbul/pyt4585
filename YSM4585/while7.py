#sayısal loto benzersiz 6 adet 8 kolon 


from random import randint


counter = int(input("Lütfen kolon sayısı yazınız:"))
index = 0

while index < counter:
    sayilar = []
    i= 0 
    while i < 6 :
        sayi = randint (1,50)
        if sayi in sayilar :
            i -= 1 #benzersiz dediğimiz için, bir sayı çıkınca diziye tekrardan eklenmiyo diye -= yaptık -- 6 tane benzersiz sayı olsun diye -- i yi bir eksiltip tekrardan process i yapıyoruz 
            #continue --da yazabilirsin 
        else :
            nmr = str(sayi)
            if (len(nmr) == 1) :
                sayilar.append("0"+str(sayi))
            else:
                sayilar.append(str(sayi)) 
        i += 1 
 
    sayilar.sort()
    print(f"{index+1}.kolon =","-".join(sayilar)) 
    index += 1 



