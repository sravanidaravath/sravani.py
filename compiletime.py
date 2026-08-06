class vehicle:
    def display__info(self):
        print("this is a vehicle")
class car(vehicle):
    def dispaly__info(self):
        print("this is a car")
class bike(vehicle):
    def dispaly__info(self):
        print("this is a bike")
V = vehicle()
C = car()
B = bike()
V.display__info()
C.dispaly__info()
B.display__info()               