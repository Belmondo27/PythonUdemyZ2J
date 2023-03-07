class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sound = "wrr"
            
    def __str__(self):
        return "Pies ma na imię " + str(self.name) + " ma " + str(self.age) + " lat."

    def speak(self):
        print("Pies o imieniu " + str(self.name) + " wydaje dźwięk " + str(self.sound))
    
    

class GoldenRetriever(Dog):
    def changeSound(self):
        self.sound = "yabadadu"


golden = GoldenRetriever("Szarik", 11)
print(golden)
golden.changeSound()
print(golden.sound)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def printInfo(self):
        print("The ", self.color, " car has ", self.mileage, " miles.")

    def drive(self):
        self.mileage = 100
        print("Aktualny przebieg to:", self.mileage)


bluecar = Car("Blue", 20000)
redcar = Car("Red", 30000)

#bluecar.printInfo()
#redcar.printInfo()

#bluecar.drive()
#print(redcar.mileage)



