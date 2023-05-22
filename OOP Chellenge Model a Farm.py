class Animal:
    def __init__(self, name, species, continent):
        self.name = name
        self.species = species
        self.continent = continent
    def printInfo(self):
        print("Animal Info: ", self.name, self.species, self.continent)


class Horse(Animal):
    def __init__(self, name, species, continent, legs ):
        super().__init__(self, name, species, continent)
        self.legs = legs
       
    def printHorseInfo(self):
        print("Horse Info: ", self.name, self.species, self.continent, self.legs, self.hooves)


class Eagle(Animal):
       def __init__(self, name, species, continent, wings, claws ):
        super().__init__(self, name, species, continent)
        self.wings = wings
        self.claws = claws

class Shark(Animal):
    def __init__(self, name, species, continent, fins, fangs ):
        super.__init__(self, name, species, continent)
        self.fins = fins
        self.fangs = fangs



standardAnimal = Animal("Zwierze", "Ssak", "Africa")
standardAnimal.printInfo()


