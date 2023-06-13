import os

print("Current working directory: ", os.getcwd())

files = os.listdir(".")
# print(files) current working dir

files = os.listdir("./Python3")
print(files) 

files = os.listdir("./basics/05 OOP/import")
print(files) 

files = os.listdir("..")
print(files) 

files = os.listdir("../Z2J_New_Project_Rock_Paper_Scissors")
print(files) 