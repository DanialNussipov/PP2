'''
Implement a generator called squares to yield the square of all numbers from (a) to (b).
Test it with a "for" loop and print each of the yielded values.
'''
def square(a, b):
    
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("A: "))
b = int(input("B: "))

for i in square(a, b):
    print(i, end = " ")