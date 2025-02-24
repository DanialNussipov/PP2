#Write a python program to convert snake case string to camel case string.
import re
     
def SnakeToCamel(text):
     
     pattern = r'_([a-zA-Z])'
     text = re.sub(pattern, lambda match: match.group(1).upper(), text)
     return text

text = input("Enter the text: ")
print(SnakeToCamel(text))