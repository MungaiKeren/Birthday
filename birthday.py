# import the three main classes from datetime
from datetime import date, time, datetime, timedelta

fname = input("Type in your first name: ")
lname = input("Your last name: ")
print("Hello "+fname+" "+lname)

while True:
    try:
        birthyear = input("What year were you born?")

    except ValueError:
        print("Sorry I didn't understand that")
        continue
    
    if birthyear == " ":
        print("Please enter an year")
        continue
    elif len(birthyear) != 4:
        print("Please give a valid birth year eg 1999")
        continue
    else:
        # input successfully parsed
        break

while True:
    try:
        birthmonth = input(" What Month?")
    except ValueError:
        print("Sorry I didn't understand that")
        continue
    if birthmonth == " ":
        print("Please enter a month in the calendar")
        continue
    elif birthmonth != "Jan" or birthmonth != "Feb" or birthmonth != "Mar" or birthmonth != "Apr" or birthmonth != "May":
        print("Please type in a valid month eg Feb")
        continue
    else:
        # input successfully parsed
        break
        

# convert the string dates to integers
int_year = int(birthyear)
int_month = int(birthmonth)

birthday = input("Day?")
c_date = int(birthday)

birthdate = date(year=int_year, month=int_month, day=c_date)

print("Birthdate: ", birthdate) # date function 'combines' the dates
today = date.today()
age = birthdate - today

print(int(age.days)//365, abs(12 - (birthdate.month - today.month)), abs(today.day))

