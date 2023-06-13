
import os

fh = open("C:\\Users\\Belmondo\\Documents\\GitHub\\PythonUdemyZ2J\\test.txt", "r")


print(__file__)
script_dir = os.path.dirname(__file__)
print("Ściezka do pliku to: ", script_dir )
print(os.getcwd())

lines = fh.readlines()
fh.close()

for line in lines:
    print(line)
