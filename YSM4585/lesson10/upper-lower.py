

# .lower() => tüm metni küçük harfe 
# .upper() => tüm metni büyük harfe 


metin = "bilge ADAM"
print(metin.lower())
#bilge adam



print("-"*50)
print(metin.upper())
#--------------------------------------------------
# BILGE ADAM

result = metin.lower().islower() # metin içerisinde yer alan tüm elemanlar küçük harf olup olmadığını kontrol eder geriye true ya da false değeri teslim eder 
print(result)
#True


result = metin.upper().isupper() 
print (result)
#True
