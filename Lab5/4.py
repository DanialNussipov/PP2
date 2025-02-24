'''
Write a Python program to find the sequences of one
upper case letter followed by lower case letters
'''
import re

def UpperLower(text):
     
     pattern = r'^.*[A-Z][a-z].*$'
     if re.fullmatch(pattern, text):
          return True
     return False

text = input("Enter the text: ")

print("It matches" if UpperLower(text) else "It's not(")