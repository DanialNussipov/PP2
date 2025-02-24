#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

def ReplaceSpace(text):
     
     pattern = r"[ ,.]"
     text = re.sub(pattern, ':', text)
     return text

text = input("Enter the text: ")

print(ReplaceSpace(text))