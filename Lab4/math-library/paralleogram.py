'''
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
'''
def area():
    
    base = int(input("Enter base of parallelogram: "))
    height = int(input("Enter height: "))
    area = base * height
    
    return f"Area of parallelogram: {area:.1f}"

print(area())

