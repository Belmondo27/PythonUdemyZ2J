list = ["Ola", "Ania", 23, 99, "Rafał"]
print( type(list))
print(list)

print(list[0])
print(len(list))
print(list[4])
print(list[len(list)-1]) #ostatni element w liscie

print(list[-1])
print(list[-2])

print(list[1:4]) #wybrane elementy z listy 
print(list[2:]) #wybrane elementy do końca listy

list[0] = "Kasia"  #podmiana zawartosci w liście
print(list)

del list[2] # usuwanie elementu z listy
print(list)

print(99 in list) #czy dana wartosc jest w liscie (true or false)
print( "Rafał" in list)
print( "Ola" in list)

if "Ania" in list:
    print("Ania jest w liście list")
    print("Kolejny kod")
if "Ania2" in list:
    print("Ania jest w liście list") #nie wykona się bo nie ma w liście

print("Dalszy kod")


for v in list:
    print(v)


data = [
       ["Daniel", "Rafał"],
       ["Kasia", "Ania"  ],
       ["Ola", "Adam"]
]
print(len(data))

print(data[1][0])
print(data[2][1])

data1 = [1, 2, 3]
data2 = [4, 5, 6]
numbers = data1 + data2
print(numbers)

numbersx2 = numbers * 2
print(numbersx2)