class Car:
    def __init__(self, brand, name, color, year):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year
        self.mileage = 1
        self.setTopSpeed(230)
 #      print("Wywołanie konstruktora ", self.brand, self.name)
        self.printInfo()

    def printInfo(self):
        print(self.brand, self.name, self.color, self.year, self.mileage, self.TopSpeed)

    def setTopSpeed(self, newTopSpeed):
        self.TopSpeed = newTopSpeed




mustang = Car("Ford", "Mustang", "Red", 1970)

mustang.mileage = 100
mustang.setTopSpeed(235)
mustang.printInfo()

charger = Car("Dodge", "Charger", "Blue", 1971)
charger.setTopSpeed(232)
charger.printInfo()

