class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model

    def get_model(self):
        return self.__model

    def fullName(self):
        return f"{self.__brand} - {self.__model}"


tataCar = Car("Tata","Nexon")
# print(tataCar.__model)
# print(tataCar.__brand)
print(tataCar.fullName())
print(tataCar.get_model())