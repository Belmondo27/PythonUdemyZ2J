class SimCard:
    def __init__(self) -> None:
        self.contacts = []
       
    def addContact(self, name, telephone):
        if isinstance(name, str) == False: return
        if isinstance(telephone, int) == False: return

        user = {
            "name" : name,
            "telephone" : telephone
                }
        self.contacts.append(user)
      

    def showContacts(self):
        for c in self.contacts:
            print(c["name"] + " " + str(c["telephone"]))


    
sim = SimCard()
sim.addContact("Ola", 123456)
sim.addContact("Adam", 123456)
sim.addContact(100, 123456)
sim.addContact("Asia", "numer")
sim.showContacts()
