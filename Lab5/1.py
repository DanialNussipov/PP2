#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

def MatchAB(text):

     pattern = r"^ab*$"
     if (re.fullmatch(pattern, text)):
          return True
     else:
          return False

text = input("Enter the text: ")

print("It matches" if MatchAB(text) else "It's not(")