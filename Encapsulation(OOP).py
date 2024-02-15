class Parent:
    def __init__(self,Name,FatherName):
        self.__Name = Name
        self.FatherName = FatherName

p1 = Parent("Shihab","Munim")
print(p1.Name)