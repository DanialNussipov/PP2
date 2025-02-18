#Write a Python program to calculate two date difference in seconds.
import datetime

def difference():
    
    today = datetime.datetime.now()
    day = datetime.datetime(2025, 1, 1)
    
    difference = abs(int((today - day).total_seconds()))

    return f"{difference} second passed from New Year:)"

print(difference())
    