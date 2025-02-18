'''Implement a generator that returns all numbers from (n) down to 0.'''

def func(number):
    
    for i in range (number, -1, -1):
        yield i
        
number = int(input("Enter the number: "))
for i in func(number):
    print(i, end = " ")