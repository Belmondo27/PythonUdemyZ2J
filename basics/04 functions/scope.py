number = 12

def test1():
    print(number)

test1()

def test2():
    number = 100
    print(number)
    if 1 == 1:
        print(number)
        if 2 == 2:
            number = 50
            print(number)
    print(number) 

test2()
print(number)


print(" \n test3")

def test3():
    global number
    number = 5
    print("test3", number)
    if 1 == 1:
        number = 6
        print("test3", number)

test3()
print("global number after test 3", number)


print("\n test4")
number = 10
def test4(number):
    print("test4 param: ", number)
    number = 20
    print("test 4 after change: ", number)


test4(33)
print("number after test 4", number)

print("\ntest5")

number = 10
def foo():
    print("foo() number ", number)

def bar():
    number = 9
    print("bar() number: ", number)
    foo()

bar()
print("global number after foo() bar(): ", number)


print("\n check1 & check2")

number = 10

def check1():
    number = 12
    print("bar() number: ", number)
    def check2():
        print("foo() number ", number)
    check2()

check1()
print("global number after check1: ", number)


print("\n if test")

if 1 == 1:
    data = 100 # zmienna globalna

print("data in global scope: ", data)

if 2 == 1:
    nextData = 15

#print("nextData in global scope:", nextData) błąd
