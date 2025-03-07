import os

path = r'C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab6'

if not os.path.exists(path):
     print(f"Error: The path '{path}' does not exist.")
else:
     a = os.listdir(path)
     for item in a:
          full_path = os.path.join(path, item)
          print(f"Item: {item}")
          print(f"  Exists: {'Yes' if os.access(full_path, os.F_OK) else 'No'}")
          print(f"  Readable: {'Yes' if os.access(full_path, os.R_OK) else 'No'}")
          print(f"  Writable: {'Yes' if os.access(full_path, os.W_OK) else 'No'}")
          print(f"  Executable: {'Yes' if os.access(full_path, os.X_OK) else 'No'}")

