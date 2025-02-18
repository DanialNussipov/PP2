'''
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
'''
def trapezoid():
    
    height = int(input("Enter height: "))
    first_base = int(input("Enter first base: "))
    second_base = int(input("Enter second base: "))
    
    MidLine = (first_base + second_base) / 2
    area = MidLine * height
    
    return f'Area of trapezoid is {area:.1f}'

print(trapezoid())
    
        

    