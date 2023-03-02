import random

class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOfStudy = None

    def printInfo(self):
        print(self.name, self.surname, self.age, self.city, self.schoolName, self.fieldOfStudy)


class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentsList = []
        self.fieldsOfStudy = ["IT", "Maths", "Robotics"]

    def addStudent(self, student):
        if isinstance(student, Student):
            self.studentsList.append(student)
            student.schoolName = self.name
            student.fieldOfStudy = random.choice(self.fieldsOfStudy)

    def printSchoolInfo(self):
        print("School name: ", self.name, " City: ", self.city)
        print("Students: ")
        for el in self.studentsList:
            el.printInfo()

 

student1 = Student("Kasia", "Lis", 20, "Krk")
student1.schoolName = "Tech School 200"
student1.country = "Poland"
student1.printInfo()
print(student1.country)
#student2 = Student("Adam", "Kowalski",33, "wawa")

school = School("Czysta", "Waw")

school.addStudent(student1)
#school.addStudent(student2)
print()
school.printSchoolInfo()