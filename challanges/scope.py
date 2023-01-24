employees = []

def addEmployee(email, salary):
    e = {
        "email" : email,
        "salary" : salary
    }

    employees.append(e)

addEmployee("ania@test.com", 6000)
addEmployee("adam@test.com", 8000)
addEmployee("kasia@test.com", 10000)

#np pctIncrease 20%
def increaseSalary(employees, pctIncrease):
    pctIncrease *= 0.01

    for e in employees:
        e["salary"] *= 1 + pctIncrease

    
increaseSalary(employees, 20)

print(employees)