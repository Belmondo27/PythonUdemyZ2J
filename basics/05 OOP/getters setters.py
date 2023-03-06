class Vehicle():
    def __init__(self):
        pass

    @property
    def gears(self):
        print("getter: ", self.__gears)
        if (self.__gears > 0 ):
            return self.__gears
        else:
            return -1
    
    @gears.setter
    def gears(self, newGears):
        print("newGears: ", newGears)
        if (newGears > 0): self.__gears = newGears

    
 
vehicle1 = Vehicle()
vehicle1.gears = 8
print(vehicle1.gears)