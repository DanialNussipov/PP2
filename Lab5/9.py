#Write a Python program to insert spaces between words starting with capital letters.
import re

def SplitUpper(text):
     
     pattern = r"(\w)(?=[A-Z])"
     text = re.sub(pattern, r"\1 " ,text)
     return text

text = input("Enter the text: ")

print(SplitUpper(text))
