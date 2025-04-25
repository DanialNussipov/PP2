name = input("enter name: ")
age = input("enter age: ")
age = int(age)
if age >= 18:
    print (f"name: {name}, age: {age}, Status: you are an adult")
else:
    print (f"name: {name[::-1]}, age: {age}, Status: you are an minor")
    

