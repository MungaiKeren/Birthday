import datetime
birthyear = input("What year were you born?")
birthmonth = input("What Month?")
birthday = input("Day?")

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


date_validation(int(birthday), int(birthmonth), int(birthyear))