# Write a Python program to print yesterday, today, tomorrow.
import datetime

def YesterdayTodayTomorrow():
    
    today = datetime.datetime.now()
    day = datetime.timedelta(days = 1)
    
    tomorrow = today + day
    yesterday = today - day
    
    print(f"Yesterday: {yesterday.strftime('%Y, %B, %d')}")
    print(f"Today: {today.strftime('%Y, %B, %d')}")
    print(f"Tomorrow: {tomorrow.strftime('%Y, %B, %d')}")
    
YesterdayTodayTomorrow()