class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print("Person constructor!")

    def printPersonData(self):
        print("Person.printPersonData: ", self.name, self.surname, self.city)

class Employee(Person):
    def __init__(self, name, surname, city, companyName, salary):
        Person.__init__(self, name, surname, city)
        self.companyName = companyName
        self.salary = salary

        print("Emplyee constructor!")

    def printEmployeeData(self):
        print("Employee.printEmployeeData: ", self.name, self.surname, self.city, self.companyName, self.salary)

class Manager(Employee):
    def __init__(self, name, surname, city, companyName, salary, department):
       Employee.__init__(self, name, surname, city, companyName, salary)
       self.department = department
       print("Manager constructor!")

    def hireEmployee(self):
        print("Hire Employee ")
        
    def printManagerData(self):
        print(self.name, self.surname, self.department)


person1 = Person("Ola", "Kowalska", "Krk")
person1.printPersonData()
print("")
employee1 = Employee("Kasia", "Kot", "Waw", "Tech Ltd", 10000)
employee1.printPersonData()
employee1.printEmployeeData()

manager1 = Manager("Ania", "X", "Waw", "Tech2 Ltd", 5000, "IT")
manager1.printPersonData()
manager1.printEmployeeData()
manager1.printManagerData()