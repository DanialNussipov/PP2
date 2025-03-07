import os

def analyzepath(givenPath):
     
     if os.path.exists(path):
          print("The path exists.")
          filename = os.path.basename(path)
          directory = os.path.dirname(path)
          print("Filename:", filename)
          print("Directory:", directory)
     else:
          print("The path does not exist.")
        
path = r'C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab6'
analyzepath(path)