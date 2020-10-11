# dışarıdan girilen metin içerisinde yer alan tüm karakterlerin ascii kod değerlerinin toplamını ekrana yazdırınız 


def metintoplamdeger(string):
    string = string.replace(" ", "")
    havuz = 0
    for i in list(string) :
        havuz += ord(i)
        return havuz 
total = metintoplamdeger(
    input("lütfen metin giriniz:")
)
print(total) 






file1 = "ba.png"
file2 = "ba.jpg"
file3 = "ba.gif"
file4 = "ba.png"
file5 = "ba.tff"
file6 = "ba.mp3"
file7 = "ba.mp4"
file8 = "ba.jpg"
file9 = "ba.gif"
file10 = "ba.png"
file11 = "ba.gif"

# # yukarıda yer alan dosyalar içerisinde .png olanların sayısını ekrana yazdırınız 


#1.
toplam = list(filter(lambda x: x in x, ["png","xlsx", "docx"]))
print(len(toplam))


#2.
def kontrol(*param) :
    count = 0 
    for i in param: # for key, value in param.items() -------------> da yazılabilir 
        retVal = i.endswith("png")
        if retVal :
            count += 1 
        return count 
result = kontrol( file1 ,
file2 ,
file3 ,
file4 ,
file5 ,
file6 ,
file7 ,
file8 ,
file9 ,
file10 ,
file11 )
print(kontrol)
