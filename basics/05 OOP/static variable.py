class Employee:
    "Emplloyee class describing company employee"
    numEmployees = 0
    employeesList = []

    def __init__(self, name):
        "Constructor for Employee"
        self.name = name
        Employee.numEmployees += 1
        print(self.name, "numEmployees: ", Employee.numEmployees)

        Employee.employeesList.append(self)


    def printAllEmplpoyees(self):
        for el in Employee.employeesList:
            print(el.name)



employee1 = Employee("Sylwek")
employee1 = Employee("Kasia")

employee1 = Employee("Adam")
employee1 = Employee("Karol")

print("Employee.numEmployees: ", Employee.numEmployees)

print(" ")

employee1.printAllEmplpoyees()

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)

print(" name attr in Employee: ", hasattr(employee1, "name"))
print(" name attr in Employee: ", hasattr(employee1, "city"))
employee1.city = "Krk"
print(" name attr in Employee: ", hasattr(employee1, "city"))

print("employee1.name: ", getattr(employee1, "name"))