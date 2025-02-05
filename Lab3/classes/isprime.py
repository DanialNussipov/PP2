class List():
    def __init__(self, numbers):
        self.numbers = numbers
        
    def isprime(self, number):
        if number < 2:
            return False
        for i in range (2, int(number * 0.5 + 1)):
            if number % i == 0:
                return False
        return True     
    
    def filter_primes(self):
        return list(filter(lambda x: self.isprime(x), self.numbers))
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 11, 54, 67, 90]
myList = List(numbers)
print(myList.filter_primes())