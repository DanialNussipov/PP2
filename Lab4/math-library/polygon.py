'''
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
'''
import math

def polygon():
    
    sides = int(input("Enter number of sides: "))
    length = int(input("Enter the legth of the sides: "))
    
    area = ((sides * pow(length, 2)) / 4) * (math.sin(math.pi / sides)/math.cos(math.pi / sides))
    
    return f'Area of your polygon is {area:.2f}'

print(polygon())