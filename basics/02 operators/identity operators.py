#operatory tożsamości

strData = "test"

print( dir (strData))
print( strData.upper())

intData = 10
print(dir (intData))

a = [1,2,3,4,5]
b = a

print(a is b)

a.append(77)
print(a)
print(b)

print( a is not b) #false

c = [3,4,5]
print(a is c) #false
print(a is not c) #true