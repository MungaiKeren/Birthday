# import the three main classes from datetime
from datetime import date, time, datetime, timedelta

fname = input("Type in your first name: ")
lname = input("Your last name: ")
print("Hello "+fname+" "+lname)

birthyear = input("What year were you born?")
converted_year = int(birthyear) # int function converts string input to integer

birthmonth = input("Month?")
c_month = int(birthmonth)

birthday = input("Day?")
c_date = int(birthday)

birthdate = date(year=converted_year, month=c_month, day=c_date)

print("Birthdate: ", birthdate) # date function 'combines' the dates
today = date.today()
age = birthdate - today()
print(age) # prints age in days
print(int(age.days)//365, abs(12 - (birthdate.month - today.month)), abs(today.day))

