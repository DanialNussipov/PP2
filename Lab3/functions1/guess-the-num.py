import random 

def GuessTheNumber():    
    
    number = random.randint(1, 20)
    name = input("Hello, what is your name? ")
    print(f'Well, {name}, i am thinking of a number between 1 and 20.')
    counter = 0
        
    while True:
        attempt = int(input("Take a guess: "))
        counter += 1
        
        if attempt > number:
            print("Your guess is too high.")
        elif attempt < number:
            print("Your guess is too low.")
        else:
            print(f'Good job, {name}! You guessed my number in {counter} guesses!')
            break
        
GuessTheNumber()