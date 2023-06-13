import os
import pickle

scriptDir = os.path.dirname(__file__)

class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city

    def __str__(self):
        return str(self.name) + " " + str(self.surname) + " " + self.city
    



person1 = Person("Ola", "Kowalska", " Krk")
person2 = Person("Adam", "Kot", " Waw")
person3 = Person("Kasia", "Kot", " Gd")

people = [person1, person2, person3]

fh = open(scriptDir + "/people.dat", "wb")
pickle.dump(people, fh)
fh.close()

fh = open(scriptDir + "/people.dat", "rb")
listFromFile = pickle.load(fh)
fh.close()

print(listFromFile)

for person in listFromFile:
    print(person)