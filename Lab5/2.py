#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

def TwoToThreeB(text):
     
     pattern = r"^ab{2,3}$"
     if (re.fullmatch(pattern, text)):
          return True
     return False

text = input("Enter the text: ")

print("It matches" if TwoToThreeB(text) else "It's not(")