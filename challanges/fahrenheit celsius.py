def cToF (f):
    return f * 9 /5 + 32

def fToC (c):
    return (c - 32) * 5 / 9

print(str(cToF(20)) +  " \xB0F")
print(str(fToC(86)) +  " \xB0C")