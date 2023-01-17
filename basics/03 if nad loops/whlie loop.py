
number = 5

while number > 0:
    print(number)
    number -= 1

number = 1

while number < 6:
    print(number)
    number += 1

num = 0
while True:
    print("Wprowadź liczbę lub exit aby zakończyć ")
    strData = input()
    if strData == "exit": break
    num += int(strData)
    print("Wartość po dodatniu liczby: " + str(num))


number = 3
while number > 0:
    print(number)
    number -= 1
else:
     print("number po pętli: " + str(number))