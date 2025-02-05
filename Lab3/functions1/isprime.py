def isprime(number):
    if number < 2:
        return False
    for i in range (2, int(number * 0.5 + 1)):
        if number % i == 0:
            return False
    return True

def filter_prime(list):
    prime_list = []
    for i in list:
        x = isprime(i)
        if x == True:
            prime_list.append(i)
    print (prime_list)

list = []
while True:
    number = input("write number or press 'q' to stop: ")
    if number == 'q': 
        break

    try:
        number = int(number)
        list.append(number)
        print (f"List contains: {list}")
    except ValueError:
        print ("write number or press 'q' to stop: ")
    
filter_prime (list)