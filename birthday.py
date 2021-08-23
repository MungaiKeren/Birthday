# import the three main classes from datetime
from datetime import date, time, datetime

fname = input("Type in your first name: ")
lname = input("Your last name: ")
print("Hello "+fname+" "+lname)

birthyear = input("What year were you born?")
converted_year = int(birthyear) # int function converts string input to integer

birthmonth = input("Month?")
c_month = int(birthmonth)

birthdate = input("Day?")
c_date = int(birthdate)

print("Birthdate: ", date(year=converted_year, month=c_month, day=c_date)) # date function 'combines' the dates



