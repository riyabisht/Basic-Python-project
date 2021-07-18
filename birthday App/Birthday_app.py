import datetime
def header():
    print("___________________________")
    print(" BIRTHDAY APP")
    print("___________________________")

def enter_birthday():
    global Today
    Today= datetime.date.today()

    year=int(input("what year were you born [YYYY]?"))
    month=int(input("What month were you born[MM]?"))
    day=int(input("What day you were born[DD]?"))

    global birthday
    birthday=datetime.date(year,month,day)
    print("It looks like you were born on {0}".format(birthday))



def my_calculator():
    date=datetime.date(Today.year,birthday.month,birthday.day)
    days_left=date-Today
    return days_left.days

def birthday_info():
    days_left=my_calculator()
    if(days_left<0):
        print("You have your birthday {0} days ago this year".format(-days_left))
    elif(days_left>0):
        print("Your bithday is in {0} days ".format(days_left))
    else:
        print("Happy Birthday!!")



def main():
    header()
    enter_birthday()
    birthday_info()


main()

