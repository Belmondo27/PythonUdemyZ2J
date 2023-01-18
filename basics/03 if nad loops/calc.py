num = 0
operation = None
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int(input("Podaj liczbę startową: "))
        reset = False

    operation = input("Podaj operację arytmetyczną jak np. " + str(calcOperations) + " lub exit jeśli konieć lub reset: ")
    if operation == "exit": break
    if operation == "reset":
        reset = True
        continue


    if not operation in calcOperations:
        print("Wprowadzona została błędna operacja")
        continue


    secondNum = int(input("Podaj drugą liczbę: "))

    if operation == "+":
        result = num + secondNum
    if operation == "-":
        result = num - secondNum
    if operation == "*":
        result = num * secondNum
    if operation == "/":
        result = num / secondNum
    if operation == "**":
        result = num ** secondNum

    print("Wynik operacji ", str(num) + " " + operation
             + " " + str(secondNum) + " = " + str(result))

    num = result
    result = None