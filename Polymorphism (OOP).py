class Vehicle:
    def __init__(self,Model,Brand,Component):

        self.Model = Model
        self.Brand= Brand
        self.Component= Component

class Plane(Vehicle):
    pass

class Car(Vehicle):
    pass

p1=Plane("BangladeshAirplines","Us Bangla","All Component")
c1=Car("BMW","B42","All")
print(p1.Brand)
print(p1.Model,p1.Brand ,p1.Component)
print(c1.Model)
print(c1.Brand)
print(c1.Component)