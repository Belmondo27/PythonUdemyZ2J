import os

print("Absolute path to script file ", __file__)

scriptDir = os.path.dirname(__file__)
print("Absolute path to script directory: ", scriptDir)

pathtoFile = scriptDir + "\\newFile.txt"
print("Path to file: ", pathtoFile)


fh = open(pathtoFile, "w")
fh.write("content!")
fh.close()
