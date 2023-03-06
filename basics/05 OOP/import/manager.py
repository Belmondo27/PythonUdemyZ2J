from user import User, Employee

class Manager(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)

    def __str__(self):
        return "Manager: " + str(self.name)