list1 = [0,1,2,3,4,5]
print(list1[3])
print(list1[1:5])

list1[0] = 9
print(list1)


del list1[1]
print(list1)
print(len(list1))
print(max(list1))
print(min(list1))

print(list(("Ala","Ola")))

print( [0,1,2] + [3,4])
print( [0,1,2] * 3)

print( 9 in [0,1])
print( 9 not in [0,1])

list1.append(99)
list1.append(3)

print(list1)
print(list1.count(3))

list1.extend([7,6,9])
print(list1)

list1.insert(3,101)
print(list1)

print(list1.index(9))

list1.reverse()
print(list1)

list1.sort()
print(list1)

num = list1.pop()
print("num", num)
print(list1)