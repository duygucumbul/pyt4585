#programcı hataları
#program kusurları
#istisnai hataları
#mantıksal hatalar

# telefonNumarasi = int(input( "Lütfen telefon numarasını giriniz: "))
# print("Tebrikler hayatta bir kez bile olsa başarı sağladın!")


try : 
   telefonNo = int(input("Lütfen telefon numaranızı giriniz: "))
   print("Tebrikler")


except ValueError:
    print( "ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")

except: 
    print("İşlem Hatası")
