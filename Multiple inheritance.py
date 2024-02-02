class father:
    car="Lamborini"
    balance="1000"
    Home="10 floor"


class father_2:
    smartphone = "Iphone"
    AC="Walton"
    Microphone="Fifine"
class father_3:
    webcome="Icam"
    Laptop="Asus"
class uncle(father,father_2,father_3): #inheritance happens here
    broken_phone=""
    old_home=""

u=uncle()
print(u.car)
print(u.webcome)
print(u.smartphone)
