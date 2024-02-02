class father:
    car="Lamborini"
    balance="1000"
    Home="10 floor"


class son1(father):
    smartphone = "Iphone"
    AC="Walton"
    Microphone="Fifine"
class son2(son1):
    webcome="Icam"
    Laptop="Asus"
class son3(son2):
    brokenphone="Vivo"
    Brookenbike="Honda"

u=son3()
print(u.car)
print(u.webcome)
print(u.brokenphone)
