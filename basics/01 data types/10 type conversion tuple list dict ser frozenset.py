listaData = [1,2,3,4,5,6]

tupleData = tuple(listaData)
print(tupleData)

otherList = list( ("Ola", 23, 234) )
print(otherList)

setData = set(otherList)
print( type(setData))
print( setData)

frozenSetData = frozenset(tupleData)
print(type(frozenSetData))
print(frozenSetData)


tupleData = (("Ola", 123), ("Adam", 321))

dictData = dict(tupleData)
print(dictData)
print(dictData["Ola"])