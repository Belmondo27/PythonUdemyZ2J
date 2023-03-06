class Dog:
    def __init__(self):
        print("Konstruktor!")

    def __del__(self):
        print("Destruktor!")

dog1 = Dog()
