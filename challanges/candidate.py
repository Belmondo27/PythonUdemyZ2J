

exp = 2
lang = ["python", "typescript", "javascript", "java"]
contractType = "b2b"

if exp >= 2 and "python" in lang and "java" in lang:
    if contractType == "b2b" or contractType == "employment":
        print("Kandydat został przyjęty")
    else:
        print("Pracownik nie spełnia wymogu typu zatrudnienia ", contractType)
else:
    print("Kandydat nie spełnia podstawowych wymagań") 
