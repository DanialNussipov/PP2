import os

path =(r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab6\os-n-dir\ForcedToBeRemoved.txt")
if os.path.exists(path):
     os.remove(path)
else:
     print("the file does not exist")