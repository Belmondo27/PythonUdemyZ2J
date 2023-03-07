class Animal:
    def __init__(self, name, species, continent):
        self.name = name
        self.species = species
        self.continent = continent
    def printInfo(self):
        print("Animal Info: ", self.name, self.species, self.continent)


class Horse(Animal):
    def __init__(self, name, species, continent, legs, hooves ):
        Animal.__init__(self, name, species, continent)
        self.legs = legs
        self.hooves = hooves
    def printHorseInfo(self):
        print("Horse Info: ", self.name, self.species, self.continent, self.legs, self.hooves)


class Eagle(Animal):
       def __init__(self, name, species, continent, wings, claws ):
        Animal.__init__(self, name, species, continent)
        self.wings = wings
        self.claws = claws

class Shark(Animal):
    def __init__(self, name, species, continent, fins, fangs ):
        Animal.__init__(self, name, species, continent)
        self.fins = fins
        self.fangs = fangs



standardAnimal = Animal("Zwierze", "Ssak", "Africa")
standardAnimal.printInfo()

horse1 = Horse("Koń", "Ssak", "Europa","Cztery nogi", "Cztery Kopyta")
horse2 = Horse("Koń2", "Ssak", "Asia","3 nogi", "5 Kopyta")
horse1.printInfo()
horse1.printHorseInfo()
horse2.printInfo()
horse2.printHorseInfo()