



def metot(ad,soyad,mail,gorev,*telefonlari):
    print("""
    Personalein adı         : {}
    Personalin soyadı       : {}
    personalin mail adresi  : {}
    personalin görevi       : {}
    personalin telefonları  : {}
    """. format (ad,soyad,mail,gorev,"-".join(telefonlari)))

metot("murat", "vuranok", "murat.vuranok", "danışman", "telefon no","2345678","345678")