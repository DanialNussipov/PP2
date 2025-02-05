def convert ():
    farenheit = int (input("input temperature in Farenheit: "))
    celsium = (5 / 9) * (farenheit - 32)
    print(f"temperature in Celsium is: {celsium:.1f}")
convert()    