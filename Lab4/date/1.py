# Write a Python program to subtract five days from current date.
import datetime

def subtraction():
    
    current = datetime.datetime.now()
    days = datetime.timedelta(days = 5)
    past = (current - days).strftime("%Y, %B, %d")
    
    return past

print(subtraction())