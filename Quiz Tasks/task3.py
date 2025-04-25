def square (num):
    return num ** 2
a = int(input())
print(square (a))

class Person():
    def __init__(self, fname, age):
        self.fname = fname
        self.age = age
    def greet(self):
        print (f"hello, my name is {self.fname}, i am {self.age} years old!")
p = Person ("Danial", 18)
p.greet()
        
class Uni(Person):
    def __init__(self, fname, age, uni):
        super().__init__(fname, age)
        self.uni = uni
    def greet(self):
        print (f"hello, my name is {self.fname}, i am {self.age} years old! I study in {self.uni}")
p = Uni("Danial", 18, "kbtu")
p.greet()