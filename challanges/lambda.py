names = ["Ola", "Ania", "Kasia"]

result = list( map(lambda a: a + " Kowalska", names))
print(result)

result2 = list( filter(lambda a: len(a) > 12, result))
print(result2)