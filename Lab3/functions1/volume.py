def volume():
    radius = int(input("enter the radius of sphere: "))
    pi = 3.14
    volume = 4/3 * pi * pow(radius, 3)
    print(f"volume of the sphere is: {volume:.2f}")
volume()