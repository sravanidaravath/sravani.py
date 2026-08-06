class Vehicle:
    def __init__(self, brand,speed):
        self.brand = brand
        self.speed = speed

    def display__info(self):
            print("Brand:", self.brand)
            print("Speed:", self.speed)

class Car(Vehicle):
    def display__info(self):
         print("Car Brand", self.brand)
         print("Maximum Speed",self.speed,"km/h")

class Bike(Vehicle):
     def display__info(self):
          print("Bike Brand",self.brand)
          print("Maximum speed",self.speed,"km/h")

car = Car("hyundai", 180)
bike= Bike("yamaha",140)
car.display__info()
bike.display__info()