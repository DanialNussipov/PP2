import time
import math

def myfunc(num, milisec):
     
    time.sleep(milisec / 1000) 
    result = math.sqrt(num)
    return result

num = int(input())
milisec = int(input())
answer = myfunc(num, milisec)
print(f"Square root of {num} after {milisec} miliseconds is", answer)