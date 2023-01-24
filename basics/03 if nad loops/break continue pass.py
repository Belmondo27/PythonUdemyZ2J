data = [0,1,2,3,4,5]

for v in data:
    if v == 3:
          break
    print(v * 2)


print("")

for v in data:
    if v == 3 or v == 5:
        continue
    print(v)

if 10 > 2:
    print("10 > 2")
else:
    pass