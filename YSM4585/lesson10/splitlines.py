

# .splitlines() = her bir alt satırdaki elemanların aralarına (,) karakteri ekler

# NOT : metin altta yer alan örnek gibi yazıldıysa geçerlidir

metin = """bilge
adam
beşiktaş
şubesi
pyhton 
dersleri
"""
print(metin.splitlines())
#['bilge', 'adam', 'beşiktaş,şubesi', 'pyhton ', 'dersleri']




metVal = "bilge\nadam beşiktaş şubesi python dersleri"
print (metVal.splitlines())
#['bilge', 'adam beşiktaş şubesi python dersleri']



# NOT: parametre olarak True eklerseniz, her bir elemanın sonuna \n ekler
print(metin.splitlines(True))
# ['bilge\n', 'adam\n', 'beşiktaş\n', 'şubesi\n', 'pyhton \n', 'dersleri\n']


print("".join(metin.splitlines(True)))
#bilge
# adam
# beşiktaş
# şubesi
# pyhton 
# dersleri