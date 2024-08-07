class Car:
    def __init__(self,__brand,__model):
        self.brand = __brand
        self.model = __model

    def get_full_name(self):
        return f"{self.brand} - {self.model}"
    
    @staticmethod
    def get_static_method():
        return "Static Method Called"
    

car = Car(
    'Tata','Nexon'
)

print(car.get_full_name())  # Normal Method Called
print(Car.get_static_method())  # Static Method Called