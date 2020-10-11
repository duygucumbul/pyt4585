# # dictionary() key value formatında dataları listelemek için kullanılır . Json formatında data tutar WebApi (servisler) Javascript Angular React (js-native) gibi birçok platform desteklemektedir


personeller = [
    {
        "Id": 1,
        "firstname": "murat",
        "lastname": "vuranok",
        "mail": "murat.vuranok@bilgeadam.com",
        "phone": "6795804567",
        "phones": [
            {
                "no": "123456",
                "title": "work",
                "description": ""

            }]},
    {
        "Id": 2,
        "firstname": "duygu",
        "lastname": "cumbul",
        "mail": "duygu.cumbul@bilgeadam.com",
        "phone": "34560987654"
    }
]

print(personeller[0])

# # {"Id" : 1,"firstname" : "murat" ,"lastname" : "vuranok","mail" : "murat.vuranok@bilgeadam.com","phone" : "6795804567","phones: " ["no" : "123456","title" : "work","description" : ""}}


print(personeller[0]["phones"][0])
# # {"no" : "123456","title" : "work",  "description" : ""}

print(personeller[0]["firstname"])


users = [["ceo", "123", ], ["admin", "123"], ["user", "123"]]  # => list
kullanicilarin: list

kullanicilarin = [
    {"username": "admin", "password": "123"},
    {"username": "ceo", "password": "123"},
    {"username": "moderator", "password": "123"}
]

print(users[0])  # ceo
print(users[0][0])  # ceo
print(users[0][1])  # ceo

print(kullanicilarin[0])  # {username : admin}
print(kullanicilarin[0]["username"])  # admin
print(kullanicilarin[0]["password"])  # admin


# dictionary içerisinde yer alan bir kaydı güncellemek iisterseniz


i = 0  # hangi eleman güncellenecek
key = "firstname"
value = "şahin"

oldRecord = personeller[i][key]

personeller[i][key] = value

newrecord = personeller[i][key]
print(oldRecord)
print(newrecord)




#--------------------------------



firstname = input("Lütfen adınızı giriniz:")
lastname = input("Lütfen soyadınızı giriniz:")
# mail = input("Lütfen mailini giriniz:")
phone = input("Lütfen telefonunuzu giriniz:")

id = len(personeller)
indexNo = len(personeller) - 1

personeller.append({
    "Id": id,
    "IndexNo ": indexNo,
    "firstname": firstname,
    "lastname": lastname,
    "mail": f"{firstname}.{lastname}@bilgeadam.com",
    "phone": phone,

})
print(personeller)


# 'Id': 2, 'firstname': 'duygu', 'lastname': 'cumbul', 'mail': 'duygu.cumbul@bilgeadam.com', 'phone': '34560987654'}, .......(devamı aşağıda)
# {'Id': 2, 'IndexNo ': 1, 'firstname': 'duygu', 'lastname': 'cumbul', 'mail': 'duygu.cumbul@bilgeadam.com', 'phone': '345678'}] ...... (aşağıda çıkan yazı print dedikten sonra) ........