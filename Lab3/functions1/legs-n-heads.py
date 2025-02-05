'''
let x be chickens and y be rabbits
{x + y = heads  -> x = heads - y
{2x + 4y = legs -> 2heads + 2y = legs

heads + y = legs / 2
y = legs / 2 - heads
'''

numheads = int(input("enter number of heads: "))
numlegs = int(input("enter number of legs: "))

def solve(numheads, numlegs):
    rabbits = numlegs / 2 - numheads
    chickens = numheads - rabbits
    print (f"number of rabbits: {int(rabbits)}") 
    print (f"number of chickens: {int(chickens)}")
    
solve(numheads, numlegs) 
          
          

    
