import os
import shutil

scriptDir = os.path.dirname(__file__)

fh = open(scriptDir + "/test.txt", "w", encoding="utf-8")
fh.write("Dane ńćóśł")
fh.close()


if not os.path.exists(scriptDir + "/Newtest.txt"):
        os.rename(scriptDir + "/test.txt", scriptDir + "/Newtest.txt",)


print(os.path.getsize(scriptDir + "/Newtest.txt",))

print(os.path.isfile(scriptDir + "/Newtest.txt"))
print(os.path.isdir(scriptDir + "/Newtest.txt"))
print(os.path.isdir("./basics"))

if os.path.exists(scriptDir + "/subDir"):
      os.rmdir(scriptDir + "/subDir")

if not os.path.exists(scriptDir + "/subDir"):
    os.mkdir(scriptDir + "/subDir")


if os.path.exists(scriptDir + "/Newtest.txt"):
      os.remove(scriptDir + "/Newtest.txt")



print("current working dir ", os.getcwdb())
os.chdir(scriptDir)
print("current working dir ", os.getcwdb())


if not os.path.exists("data-copy.dat"):
      shutil.copyfile("data.dat", "data-copy.dat")