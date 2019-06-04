# Datetime 1

from datetime import date


def is_leap(ayear): # returns True if ayear is leap and False otherwise
    ayear = int(ayear)
    if ayear%400 == 0:
        return True
    elif ayear%100 == 0:
        return False
    elif ayear%4 == 0:
        return True
    else:
        return False
    
def what_day_today(): # returns the day today
    date_today = date.today() # today's date
    year_today = int(date_today.year) # this year
    month_today = int(date_today.month) # this month
    day_today = int(date_today.day) # this day in this month
    days_total = day_today # Initialize days_total
    month_ = month_today - 1 # Initianize month_ which is number of months past this year
    year_ = year_today - 1 # Initianize year_ which is number of years past
    while month_ > 0: # Looping through month_ to calculate days past this year
        if month_ == 2: # For a february 
            if is_leap(year_today): # In a leap year
                days_total += 29 # Add 29 days to days_total
            else: # Not in a leap year
                days_total += 28 # Add 28 days to days_total      
        elif month_ == 1 or month_ == 3 or month_ == 5 or month_ == 7 or month_ == 8 or month_ == 10 or month_ == 12: # For the months with 31 days
            days_total += 31 # Add 31 to days_total
        else: # For the months with 30 days
            days_total += 30 # Add 30 to days_total
        month_ -= 1 # Move to the previous month
    while year_ >= 1970: # Looping through year_ to calculate number of days past from 1970
        if is_leap(year_): # For a leap year
            days_total += 366 # Add 366 to days_total
        else: # For a year which is not leap
            days_total += 365 # Add 365 days to days_total
        year_ -= 1 # Move to the previous year
        # It was wednesday on 1st Jan 1970
    if days_total%7 == 0:
        print("Wednesday")
    elif days_total%7 == 1:
        print("Thursday")
    elif days_total%7 == 2:
        print("Friday")
    elif days_total%7 == 3:
        print("Saturday")
    elif days_total%7 == 4:
        print("Sunday")
    elif days_total%7 == 5:
        print("Monday")
    else:
        print("Tuesday")
        
what_day_today()