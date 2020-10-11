
# dışarıdan birden fazla karakter alabilir başına da sonuna da ortasında da olabilir bunları elimate et


def Customstrip(param, *chars) :
    value = param
    while True:
        if value[0] in chars:
            value = value.strip(value[0])
        else: 
            break 
    
    return value 

result = Customstrip('@?_-Bilge Adam Beşiktaş', 'q', '?', '@', 'r')
print(result) 
#_-Bilge Adam Beşiktaş




def Customstrip(param, *chars) :
    i=0                             # char in uzunluğunun karesi kadar ilerliycek çünkü hem sonda hem baştakini control etmesi gerek 
    while i < (len(chars)**2):          # iki if var çünkü hem başı hem de sonu için iki ayrı fonksiyon gerek, başta varsa sonda da herhangi bir charm olabilir 
        if param[0] in chars:               # parametrenin başında char dan bir eleman varsa sil
            param = param.strip(param[0])
        if (param[len(param) - 1] in chars):        # paarmetrenin sonunda varsa charmlardan biri sil o yüzden len alıyoruz uzunluğu bulduktan sonra geriye dönebiliyoruz 
            param = param.strip(param[len(param)-1])
        i += 1  
    
    return param 
result = Customstrip('@?_-Bilge Adam Beşiktaş', '-', '?', '@', '&')       # virgülden öncesi param, sonraları chars 
print(result) 
#-Bilge Adam Beşiktaş

