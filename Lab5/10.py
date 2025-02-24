#Write a Python program to convert a given camel case string to snake case.
import re

def CamelToSnake(text):
     
     pattern = r"(\w)(?=[A-Z])"
     text = re.sub(pattern, r"\1_" ,text)
     text = text.lower()
     return text
     
text = input("Enter the text: ")
print(CamelToSnake(text))