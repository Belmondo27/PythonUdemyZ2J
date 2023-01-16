#operatory logiczne


print( True and True) # true
print( True and False) # false
print( False and True) # false
print( False and False) # false


print( 10 >= 5 and 3 < 9) #true
print( 12 < 20 and 5 > 10) #false
print( 3 == 5 and 6 < 1) #false

taskCompleted = True
linesOfCodeWritten = 100

if taskCompleted == True and linesOfCodeWritten >= 50:
    print("Go Home")

houerOfDay = 15
if taskCompleted == True and linesOfCodeWritten >= 60 and houerOfDay >=15:
    print("Go Home")

print( True or True) #true
print( True or False) #true
print( False or True) #true
print( False or False) #false

print( 10 >= 10 or 5 > 3) #true
print( 5 <= 7 or 5 == 1) #true
print( 2 != 2 or 5 == 5) #true
print( 1 == 3 or 4 > 10) #false

if 10 > 5 or "Ania" != "Ola":
    print("true or true")

if 3 == 5 or "Ania" == "Ola":
    print("Ten kod się nie uruchomi")


print(not True) #false
print(not False) #true

print( not( 3 == 3)) #false
print( not( 5 > 10)) #true
print( not ( 10 >= 6 and "Ola" != "Ania")) #false

taskCompleted = False

if taskCompleted == True:
    print("Go home")

if not taskCompleted:
    print("Stay a bit longer and finish")
