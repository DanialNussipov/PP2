#Create a generator that generates the squares of numbers up to some number N.
def squares():
    
    number = int(input("Enter the number: "))
    gen = (i ** 2 for i in range(number))
    for i in range(number):
        print(next(gen), end = " ")
        
squares()