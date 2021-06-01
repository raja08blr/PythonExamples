class test:
    #constructor
    def __init__(self):
        self.name = input("Enter the name: ")
        print("Parent constructor method")
    def input_1(self):
        print("test class",self.name)

class b(test):
    def input_1(self):
        print("child class",self.name)

#Drivers code
obj = b()
obj.input_1()