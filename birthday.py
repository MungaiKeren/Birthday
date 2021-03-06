# import the three main classes from datetime
from datetime import date, time, datetime, timedelta

fname = input("Type in your first name: ")
lname = input("Your last name: ")
print("Hello "+fname+" "+lname)

# take the input year and validate the input

while True:
    try:
        birthyear = input("What year were you born?")

    except ValueError:
        print("Sorry I didn't understand that")
        continue
    
    if not birthyear:
        print("Please enter an year")
        continue
    elif len(birthyear) != 4:
        print("Please give a valid birth year eg 1999")
        continue
    else:
        # input successfully parsed
        break

# prompt for the month year and validate the month 

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
while True:
    try:
        birthmonth = input("What Month?")
    except ValueError:
        print("Sorry I didn't understand that")
        continue
    if not birthmonth:
        print("Please enter a month in the calendar")
        continue
    elif birthmonth not in months:
        print("Please enter a valid month eg Feb")
    else:
        # Input susscessfully parsed
        break

# prompt for month date and validate the input
while True:
    try:
        birthday = input("Day?")
    except ValueError:
        print("Sorry I do not understand that")
        continue
    if not birthday:
        print("Please enter a date of the month")
        continue
    elif int(birthday) > 31:
        print("Ensure to enter a valid date eg 29")
        continue
    elif int(birthday) <= 0:
        print("Ensure to enter a valid date eg 29")
        continue
    else:
        break
# convert the string dates to integers
int_year = int(birthyear)
int_month = months.index(birthmonth) + 1
int_birthday = int(birthday)

# validate date
import datetime
def date_validation(day, month, year):
    isValidDate = True

    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    
    if isValidDate == False:
        print("Invalid date! Try again")
    
    else:
        usersDate = date(year=int_year, month=int_month, day=int_birthday)
        print("You were born on: ", usersDate)


date_validation(int_birthday, int_month, int_year)

from datetime import datetime
from dateutil import relativedelta

usersDate = date(year=int_year, month=int_month, day=int_birthday)
this_day = datetime.today()

if usersDate.month == this_day.month:
    if usersDate.day == this_day.day:
        age = relativedelta.relativedelta(this_day, usersDate)
        print("Hurray, today is your birthday! You are now {0.years} years old".format(age))


age = relativedelta.relativedelta(this_day, usersDate)

print("You are {0.years} years, {0.months} months and {0.days} days old".format(age))

# next birthday

def calculate_dates(original_date, now):
    delta1 = datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime(now.year+1, original_date.month, original_date.day)
    
    return ((delta1 if delta1 > now else delta2) - now).days

now = datetime.now()
c = calculate_dates(usersDate, now)

print("Your next birthday is in ", c, " days.")