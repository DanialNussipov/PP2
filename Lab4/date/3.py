#Write a Python program to drop microseconds from datetime.
import datetime

def microseconds():
    
    current = datetime.datetime.now()
    print(f"Current date and time: {current}")
    
    microsecs = current.replace(microsecond = 0)
    print(f"Current date and time with no microseconds: {microsecs}")
    
microseconds()