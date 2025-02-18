'''
Define a function with a generator which can iterate the numbers,
which are divisible by 3 and 4, between a given range 0 and n.
'''
def func(number):
    
    for i in range(number + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
    
number = int(input("Enter the number: "))
mylist = [i for i in func(number)]
print(mylist)     