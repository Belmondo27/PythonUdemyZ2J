class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.topSpeed = 10
        self.numWheels = 4

    def printVehicleInfo(self):
        self.topSpeed = 230
        print("printVehicleInfo: ", self.brand, self.name, self.topSpeed, self.numWheels )

    def printNumWheels(self):
        print("Vehilce.numWheels: ", self.numWheels)

class Car(Vehicle):
   def printCarInfo(self):
       print("printCarInfo: ", self.brand, self.name, self.topSpeed, self.numWheels)

   def printVehicleInfo(self):
       self.topSpeed = 230
       print("Car.printVehicleInfo: ", self.brand, self.name, self.topSpeed, self.numWheels )


class SuperCar(Car):
    def reachSpeed300(self):
        self.topSpeed = 301
        print("Super car reached 300!")



vehicle1 = Vehicle("Ford", "Fiesta")
vehicle1.printVehicleInfo()
car1 = Car("Fiat", "Tipo")
car1.printCarInfo()
car1.printVehicleInfo()

superCar1 = SuperCar("Dacia", "Sandero")
superCar1.reachSpeed300()
superCar1.printVehicleInfo()
superCar1.printNumWheels()
