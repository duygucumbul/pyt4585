# .maketrans , .translate 


# mail adresi düzenleyen metot yazdık 

def ClearString(param):
    return param.lower().replace("ç","c").replace("ü","u").replace("ş","s").replace("ö","o").replace(" ", "")
print(ClearString("ahmet.şahin @hotmail.com"))
#ahmet.sahin@hotmail.com


kaynak = "şçğüıöŞÇĞÜİÖ"
hedef = "scguioSCGUIO"
metin = "bilge adam beşiktaş şubesi PYTHON DERSLERİ BAŞLADI"

table = str.maketrans(kaynak,hedef)
metin= metin.translate(table)
print(metin) 
#bilge adam besiktas subesi PYTHON DERSLERI BASLADI

