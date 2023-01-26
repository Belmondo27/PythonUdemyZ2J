Strnum = input("Podaj liczbę całkowitą: ")
Intnum = int(Strnum)
print(type(Strnum))
print(Strnum)
print(int(Intnum))
print(type(Intnum))

def calculateSquareArea(heigh):
    return heigh * heigh
    

print(calculateSquareArea(10))



Floatnum = input("Podaj liczbę dziesiętną: ")
Intnum2 = float(Floatnum)
KwadratIntnum2 =  calculateSquareArea(Intnum2)
print(round(KwadratIntnum2,2))