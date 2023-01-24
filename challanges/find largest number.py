def findLargest(num1, num2):
    if num1 == num2:
        print("Obie liczby są równe.")
    elif num1 > num2:
        print("Liczba ", num1, "jest większa od liczby ", num2)
        return num1
    else:
        print("Liczba ", num2, "jest większa od liczby ", num1)
        return num2


print(findLargest(3,10))

print(findLargest(12,7))
