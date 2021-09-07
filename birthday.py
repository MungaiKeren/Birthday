# import the three main classes from datetime
from datetime import date, time, datetime, timedelta

fname = input("Type in your first name: ")
lname = input("Your last name: ")
print("Hello "+fname+" "+lname)

while True:
    try:
        birthyear = input("What year were you born?")
        if not len(birthyear) == 4:
            print("Please give us a valid date, eg 1999 ")
        continue
    except ValueError:
        # age successfully parsed
        break


birthmonth = input("Month?")
c_month = int(birthmonth)

birthday = input("Day?")
c_date = int(birthday)

birthdate = date(year=int_year, month=c_month, day=c_date)

print("Birthdate: ", birthdate) # date function 'combines' the dates
today = date.today()
age = birthdate - today

print(int(age.days)//365, abs(12 - (birthdate.month - today.month)), abs(today.day))

