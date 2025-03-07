import os

def listDirectoriesFiles(path):
     
     print("Directories:")
     for whod in os.listdir(path):
          if os.path.isdir(os.path.join(path, whod)):
               print(whod)
     print("\n")

     print("Files:")
     for whod in os.listdir(path):
          if os.path.isfile(os.path.join(path, whod)):
               print(whod)
     print("\n")
            
     print("All:")
     for root, dirs, files in os.walk(path):
          for dir in dirs:
               print(os.path.join(root, dir))
          for file in files:
               print(os.path.join(root, file))
     print("\n")        
path = r'C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab6'

listDirectoriesFiles(path)