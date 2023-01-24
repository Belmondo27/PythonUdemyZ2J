employee = {
    "name" : "Adam",
    "emial" : "adam@example.com", 
    "rank" : "programmer",
    "salary" : 8000,
}

def promoteToManager(user):
    if user["rank"] == "manager":
        print("Pracownik jest już managerem")
        return
    
    user["rank"] = "manager"
    user["salary"] *= 1.50




promoteToManager(employee)
print(employee)
