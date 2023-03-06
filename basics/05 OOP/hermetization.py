class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.__gears = 5

    def __getGearsInfoStr(self):
        return "gears number " + str(self.__gears)
    
    def printInfo(self):
        print(self.brand, self.name, self.__getGearsInfoStr())

    
vehicle1 = Vehicle("Ford", "Fiesta")
#print(vehicle1.__gears) ###błąd
#vehicle1.__getGearsInfoStr() ###błąd
vehicle1.printInfo()


class Car(Vehicle):
    def __init__(self, brand, name):
        Vehicle.__init__(self, brand, name)
        print(self.__gears)


#car1 = Car("Fiat", "punto")
print(vehicle1._Vehicle__gears)
print(vehicle1._Vehicle__getGearsInfoStr())