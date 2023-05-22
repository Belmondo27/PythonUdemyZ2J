class Village:
    def __init__(self, name, population, number_of_buildings):
        self.name = name
        self.population = population
        self.number_of_buildings = number_of_buildings
    def printInfo(self):
        print("Village Info: ", self.name, " Population: ", self.population, " Number of buildings: ", self.number_of_buildings)

class Building:
    def __init__(self, name, number_of_employees):
        self.name = name
        self.number_of_employees = number_of_employees


class Factory(Building):
    def __init__(self, name, number_of_employees, number_of_machines):
        super.__init__(self, name, number_of_employees)
        self.number_of_machines = number_of_machines


class Warehouse(Building):
     def __init__(self, name, number_of_employees, capacity):
        super.__init__(self, name, number_of_employees)
        self.capacity = capacity

class House(Building):
     def __init__(self, name, number_of_employees, number_of_residents):
        super.__init__(self, name, number_of_employees)
        self.number_of_residents = number_of_residents


class Resident:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

class Santa(Resident):
     def __init__(self, name, age, occupation):
        super.__init__(self, name, age, occupation)
     def read_letter():
         pass
       

class Employee(Resident):
     def __init__(self, name, age, occupation, salary):
        super.__init__(self, name, age, occupation)
        self.salary = salary


class Reindeer(Resident):
    def __init__(self, name, age, occupation, nose_color):
        super.__init__(self, name, age, occupation)
        self.nose_color = nose_color
    def max_speed():
        pass