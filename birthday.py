# import the three main classes from datetime
from datetime import date, time, datetime, timedelta

fname = input("Type in your first name: ")
lname = input("Your last name: ")
print("Hello "+fname+" "+lname)

while True:
    try:
        birthyear = input("What year were you born?")

    except ValueError:
        # age successfully parsed
        print("Sorry I didn't understand that")
        continue
    
    if birthyear == " ":
        print("Please enter a date")
        continue
    elif len(birthyear) != 4:
        print("Please give a valid birth year")
        continue
    else:
        # input successfully parsed
        break

# convert the string dates to integers
int_year = int(birthyear)

birthmonth = input("Month?")
c_month = int(birthmonth)

birthday = input("Day?")
c_date = int(birthday)

birthdate = date(year=int_year, month=c_month, day=c_date)

print("Birthdate: ", birthdate) # date function 'combines' the dates
today = date.today()
age = birthdate - today

print(int(age.days)//365, abs(12 - (birthdate.month - today.month)), abs(today.day))

