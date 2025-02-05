class Shape():
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
class Rectangle(Shape):
    
    def area(self):
        return self.length * self.width
    
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = Rectangle(length, width)
print(f'Area of rectangle: {area.area()}')

        
        