#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

def LowerUnder(text):
     
     pattern = r"^[a-z]+_[a-z]+$"
     if re.fullmatch(pattern, text):
          return True
     return False

text = input("Enter the text: ")

print("It matches" if LowerUnder(text) else "It's not(")