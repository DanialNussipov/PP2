string = str(input("input string: "))

lower, upper = 0, 0
for char in string:
    if(char.islower()):
        lower += 1
    if(char.isupper()):
        upper +=1

print("lowercase letters:",lower)
print("upper letters:",upper)