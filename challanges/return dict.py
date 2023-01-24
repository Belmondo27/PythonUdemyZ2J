def createUser (name, contact):
    user = {"name" : name, "email" : None, "telephone" : None}

    if isinstance(contact, str):
        user["email"] = contact
    elif isinstance(contact, int):
        user["telephone"] = contact
    

    return user


user1 = createUser("Ola", "ola@example.com")
print(user1)
user2 = createUser("Kasia", 3362036)
print(user2)