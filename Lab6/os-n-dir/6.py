import string
import os

def generate_files():
     
     directory = r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab6\os-n-dir\6py-files"

     for letter in string.ascii_uppercase:
          
          filename = letter + '.txt'
          file_path = os.path.join(directory, filename)
          
          with open(file_path, 'w') as file:
               file.write(f"This is the content of file {filename}\n")
               
          print(f"File {filename} has been created.")
          
generate_files()