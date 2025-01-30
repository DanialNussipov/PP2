fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print("\n")   
for x in "banana":
  print(x)
print("\n")   
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print("\n") 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
print("\n")   
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print("\n")   
for x in range(6):
  print(x)
print("\n")   
for x in range(2, 6):
  print(x)
print("\n")   
for x in range(2, 30, 3):
  print(x)
print("\n")   
for x in range(6):
  print(x)
else:
  print("Finally finished!")
print("\n")   
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
print("\n")   
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
print("\n")    
#for loops cannot be empty, 
#but if you for some reason have a for loop with no content,
#put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass