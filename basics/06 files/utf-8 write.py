import os

scriptDir = os.path.dirname(__file__)
print(scriptDir)

fh = open(scriptDir + "/ogonki.txt", "r", encoding="utf-8")
fh.write("tekst z ogonkami: łąóżź\n")
fh.write("tekst z ogonkami: łąóżź\n")
fh.write("tekst z ogonkami: łąóżź\n")


fh.close()