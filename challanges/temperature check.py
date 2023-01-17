
raining = False
haveUbrella = False
temp = 14

if temp >= 40 or temp <= 0:
    print("Zostań w domu")
elif temp > 0 and temp < 10 and haveUbrella and raining:   #haveUbrella == True and raining == True:
    print("Możesz wyjść z parasolką")
elif raining == False and temp >= 10:
    print("Możesz wyjść bez parasolki")
else:
    print("Zostań w domu")