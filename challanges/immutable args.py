def increaseSalary(money, bonus):
    money = money * 1.20
    sum = money + bonus
    return sum

salary = 5000

newSalary = increaseSalary(salary, 1000)

print(salary)
print(newSalary)



