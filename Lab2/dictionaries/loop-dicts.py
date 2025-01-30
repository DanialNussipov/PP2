thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)
print("\n")

for x in thisdict:
  print(thisdict[x])
print("\n")

for x in thisdict.values():
  print(x)
print("\n")
 
for x in thisdict.keys():
  print(x)
print("\n")
  
for x, y in thisdict.items():
  print(x, y)
print("\n")