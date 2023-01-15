str = "Hello world!"
print(str)
print(len(str))
print( type(str))

print( str[ len(str) - 1 ])
print(str[0:5])

print( str *4)

strX3 = str * 3
print(strX3)

str2 = str + " and Hello again!"
print(str2)

print(str2[6:]) #od 6 indeksu do końca

print(str2[::3]) #wyświetlanie co 3 znak

multiLine = """Pierwsza linia 
Druga linia
Trzecia linia
"""
print(multiLine)

multiLine2 = "Pierwsza linia\nDruga linia\nTrzecia \t linia   \" \\"  #znaki ucieki, tabluacji oraz cudzysów i backslash
print(multiLine2)
