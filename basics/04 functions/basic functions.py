def addNumer(a,b):
    return a+b

def subNumber(a,b):
    return a-b

def multiplyNumber(a,b):
    return a * b

def add4number(num1, num2, num3, num4):
    result = num1 + num2 +num3 + num4
    return result

print( addNumer(10,5))

number = subNumber(100, 56)
print(number)  #44

number = multiplyNumber(33,4)
print(number) #132

sum = add4number(1, number, addNumer(10, 6), 9)
print(sum)

