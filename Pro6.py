#Calender

import calendar

def print_yearly_calendar(year):
    print(calendar.calendar(year))

year = int(input("Enter the year: "))
print_yearly_calendar(year)