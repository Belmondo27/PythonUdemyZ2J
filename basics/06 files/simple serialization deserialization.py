import os
import pickle

scriptDir = os.path.dirname(__file__)

number = 123456
listData = ["Ania", "Ola", "Kasia"]
strData = "Test ąóć"

fh = open(scriptDir + "/data.dat", "wb")
pickle.dump(number, fh)
pickle.dump(listData, fh)
pickle.dump(strData, fh)
fh.close()


fh = open(scriptDir + "/data.dat", "rb")
numberInfo = pickle.load(fh)
ListInfo = pickle.load(fh)
strInfo = pickle.load(fh)

print(numberInfo)
print(ListInfo)
print(strInfo)

fh.close()