class Laptop:
    def __init__(self, cpu, ram = 4096, gpu = "AMD", price = 2000):
        self.setCpu(cpu)
        self.setRam(ram)
        self.gpu = gpu
        self.price = price

    def setCpu(self, cpu):
        if cpu.lower() == "amd" or cpu.lower() == "intel" or cpu.lower() == "arm":
            self.cpu = cpu
        else:
            self.cpu = "unknow"

    def setRam(self, ram):
        if type(ram) == int and ram >= 2048:
            self.ram = ram
        else:
            self.ram = 2048


    def printData(self):
        print(self.cpu, self.ram, self.gpu, self.price)



laptop1 = Laptop("Intel", 16000)
laptop1.printData()

laptop2 = Laptop("AMD", 3200)
laptop2.printData()