class MyClass:
    
    def __init__(self):
        self.str = ""
    
    def getString(self):
        self.str = str(input("enter the string: "))    
    
    def printString(self):
        print(self.str.upper())

s = MyClass()
s.getString()
s.printString()