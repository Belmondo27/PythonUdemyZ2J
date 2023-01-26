def getUserInformation(name, surname, job):
    name = name.upper().strip()
    surname = surname.strip().upper()
    job = job.strip().lower()
    
    text = "Imię:" + name +  ", Nazwisko: " + surname, ",Zawód: " + job
    return text

userInfo1 = getUserInformation("Ania", "Kowalska", "Programistka")
print(userInfo1)

    

print(getUserInformation("Daniel", "Lis", "Administrator"))
