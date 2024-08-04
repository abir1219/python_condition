class Car:
    def __init__(self,__brand,__model):
        self.brand = __brand
        self.model = __model

    def get_model(self):
        return self.model

    def fullName(self):
        return f"{self.brand} - {self.model}"


tataCar = Car("Tata","Nexon")
# print(tataCar.__model)
# print(tataCar.__brand)
print(tataCar.fullName())
print(tataCar.get_model())