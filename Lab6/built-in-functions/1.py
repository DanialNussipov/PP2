import math

num = int(input("number of list components: "))
mylist = []

while num > 0:
     
     number = int(input("enter number: "))
     mylist.append(number)
     num = num - 1
     
print(math.prod(mylist))