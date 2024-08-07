class Car:
    __totalCar = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        self.__totalCar += 1

    def get_brand(self):
        return self.__brand
    
    def get_total(self):
        return self.__totalCar
    
    def get_model(self):
        return self.__model
    
    def full_name(self):
            return f"{self.__brand} - {self.__model}"
        

class TataCar(Car):
    def __init__(self,brand,model,__battery_type):
        super().__init__(brand,model)
        self.battery_type = __battery_type
    
    def get_battery_type(self):
         return self.battery_type

tataCar = Car("Tata","Nexon")
safari = Car("Tata","Nexon")
print(tataCar.get_brand())
print(tataCar.full_name())
# print(tataCar.get_battery_type())
print(tataCar.get_total())
