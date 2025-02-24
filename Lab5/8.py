#Write a Python program to split a string at uppercase letters.
import re

def SplitUpper(text):
     
     pattern = r"(?=[A-Z])"
     text = re.split(pattern, text)
     text = list(filter(None, text))
     return text

text = input("Enter the text: ")

print(SplitUpper(text))