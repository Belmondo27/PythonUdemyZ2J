num = 5

if num >= 3:
    print("num większe lub równe 3")
    print("oraz !")
if num == 5:
    print("5 = 5")
num = 200

if num == 1:
    print("num = 1")
elif num == 2:
    print("num = 2")
elif num == 5:
    print("num = 5")
elif num == 10:
    print("num = 10")
elif num == 11:
    print("num >= 11")
else:
    print("Domyślny kod, jeżli reszta porównań da False")


if 5 > 1:  print("5 > 1")

if 10 > 2:
    print("10 > 2")
    if 4 > 1:
        print("4 > 1")
        if 3 < 2:
            print("3 > 2")
        print("4 > 1 c.d")