data = {"name" : "Ola", "city" : "Waw"}
print(data["name"])
dataPostalCode = "postalCode"
data[dataPostalCode] = 12345
print(data)
print(len(data))

del data["city"]
print(data)
data.clear()
print(data)
data = {"name" : "Kasia", "city" : "Krk"}
dataCopy = data.copy()
print(dataCopy)
print(data["name"] is dataCopy ["name"] )
print (data is dataCopy)

data2 = dict.fromkeys(("name", "city", "code"))
print(data2)

data3 = dict.fromkeys(("name", "city", "code"), 0)
print(data3)

print(data2.get("X", "DEFAULT"))
print( "name" in data2)

print(data2.keys())
print(data2.values())