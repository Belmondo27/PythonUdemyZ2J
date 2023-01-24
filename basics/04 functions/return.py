def addNumbers(a,b,c):
    return a + b + c


def sumListElements(listData):
    if len(listData) == 0:
        print("Pusta lista.")
        return None
    resault = 0
    for v in listData:
        resault += v
    return resault

print(sumListElements([]))
print(sumListElements([1,2,3,4,5,6,7,8,9]))


def printList(listData):
    if len(listData) == 0:
        return
    for v in listData:
        print(v)


print(printList([]))
print(printList([6,7,8]))