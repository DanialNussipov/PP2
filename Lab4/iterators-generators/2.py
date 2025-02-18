#Write a program using generator to print the even numbers between 0 and n in comma separated form
#where n is input from console.
def even(number):
    
    mylist = []
    for i in range(number + 1):
        if i % 2 == 0:
            yield i
            
number = int(input("Enter the number: "))
print(",".join(map(str, even(number))))        