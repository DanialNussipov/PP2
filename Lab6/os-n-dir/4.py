import os

file = open(r'C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab6\os-n-dir\a.txt')
count = 0
for lines in file:
     count += 1
print(f"The file has {count} lines")