'''
Input degree: 15
Output radian: 0.261904
'''
import math

def convert():
    
    degree = int(input("input your degrees: "))
    radians = degree * (math.pi / 180)
    print(f"your degrees in radians: {radians:.6f}")
    
convert()
