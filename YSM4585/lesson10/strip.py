

# .strip() => metnin sağındaki ve solundaki boşlukları siler 


metin = " bilge adam "
print(len(metin))  #12

metin = metin.strip()
print(len(metin)) #10 



metin = "@bilge adam@"
# metot içerisinde parametre verirseniz, geeln değer içindeki metnin başında ve sonunda parametreye gelen değeri siler 
print(metin.strip('@')) #bilge adam


metin = "@bilge adam@"
print(metin.rstrip('@'))   #@bilge adam
print(metin.lstrip('@'))   #bilge adam@

