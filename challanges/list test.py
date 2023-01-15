lista = [0, 1, 2, 3, 4, 5, 6]
print(len(lista))
del lista[1]
if 3 in lista:
    print("Liczba 3 znajduje się w liście")

for v in lista:
    print(v)

for v in lista:
    print("Elementy z listy z dodatniem liczby dwa", v + 2)

for v in lista:
    print("Elementy z listy z pomnożeniem liczby przez dwa", v * 2)
