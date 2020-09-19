try:
    sayi1 = int(input("Lütfen sayı giriniz: "))
    sayi2 = int(input("Lütfen sayı giriniz: "))
    sonuc = sayi1 / sayi2

except ValueError:
    print("İşlem Hatası")

else:
    try:
        print(sayi1 / sayi2)
        print("işlem sonucu")
    except ZeroDivisionError as mahmud:
        print(mahmud)


try:
    # db connection open
    sayi = int(input("Lütfen sayi giriniz : "))
    # connection error
    print("Tebrikler!")
    # db connection close

except:
    print("Vazgeçtim")
    # db connection close

finally:
    print("her durumda bir defa tetiklenir ")
    # db connection close
    # her iki durumda da yapılması gereken işlmeleriniz var ise, bunu finallyy içerisinde yazmanız kod  tekrarını engelleyecektir.
