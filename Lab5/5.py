#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

def EndingB(text):
     
     pattern = r"^.*a.*b$"
     if re.fullmatch(pattern, text):
          return True
     return False

text = input("Enter the text: ")

print("It matches" if EndingB(text) else "It's not(")