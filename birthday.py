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
    if birthmonth == " ":
        print("Please enter a month in the calendar")
        break
    elif birthmonth not in months:
        print("Please enter a valid month eg Feb")
    else:
        # Input susscessfully parsed
        break


# convert the string dates to integers
int_year = int(birthyear)
int_month = months.index(birthmonth) + 1

# prompt for month date and validate the input
while True:
    try:
        birthday = input("Day?")
    except ValueError:
        print("Sorry I do not understand that")
        continue
    if birthday == " ":
        print("Please enter a date of the month")
        continue
    elif int(birthday) > 31:
        print("Ensure to enter a valid date eg 29")
    else:
        break


# if birthday == " ":
#     print("Give a date")
# elif int(birthday) > 31:
#     print("Please Give a valid date")

# # check if year is leap
# elif int(birthyear) % 4 == 0:
#     if int(birthyear) % 100 == 0:
#         if int(birthyear) % 400 == 0:
#             # for the month feb, number of days cannot exceed 29
#             if birthmonth == "Feb":
#                 #this year is leap
#                 int(birthday) <= 29
#             else:
#                 # this is not a leap year
#                 int(birthday) <=28
#         else:
#             # this year is not leap
#             int(birthday) <= 28
#     else:
#         # the year is leap
#         int(birthday) <= 29
# else:
#     # the year is leap
#     int(birthday) <= 29
    




# birthdate = date(year=int_year, month=int_month, day=c_date)

# print("Birthdate: ", birthdate) # date function 'combines' the dates
# today = date.today()
# age = birthdate - today

# print(int(age.days)//365, abs(12 - (birthdate.month - today.month)), abs(today.day))

