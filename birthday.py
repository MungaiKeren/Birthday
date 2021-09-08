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


# def leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 # this is a leap year
#                 if birthmonth == "Feb":
#                     birthday = range(0,30)
#             else:
#                 # this is not a leap year
#                 if birthmonth == "Feb":
#                     birthday = range(0,29)
#         else:
#             # leap year
#             if birthmonth == "Feb":
#                 birthday = range(0,30)
#     else:
#         # not a leap year
#         if birthmonth == "Feb":
#             birthday = range(0,29)


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
        print("Valid date")


date_validation(int_birthday, int_month, int_year)


# birthdate = date(year=int_year, month=int_month, day=c_date)

# print("Birthdate: ", birthdate) # date function 'combines' the dates
# today = date.today()
# age = birthdate - today

# print(int(age.days)//365, abs(12 - (birthdate.month - today.month)), abs(today.day))

