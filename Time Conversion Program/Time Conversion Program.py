print("This is a program for converting times.")

userInput01 = input("Please enter the input time type.\n1: year(y)\n2: month(m)\n3: day(d)\n4: hour()h\n5: minute(M)\n6: second(s)\n==>")
userInput01.lower()
userInput02 = ''
if userInput01 == 'y':
    userInput02 = input("Convert year yo..\n1: month(m)\n2: day(d)\n3: hour(d)\n4: minute(M)\n5: second(s) :")
elif userInput01 == 'm':
    userInput02 = input("Convert month yo..\n1: year(y)\n2: day(d)\n3: hour(d)\n4: minute(M)\n5: second(s) :")
elif userInput01 == 'd':
    userInput02 = input("Convert day yo..\n1: year(y)\n2: month(m)\n3: hour(d)\n4: minute(M)\n5: second(s) :")
elif userInput01 == 'h':
    userInput02 = input("Convert hour yo..\n1: year(y)\n2: month(m)\n3: day(d)\n4: minute(M)\n5: second(s) :")
elif userInput01 == 'M':
    userInput02 = input("Convert minute yo..\n1: year(y)\n2: month(m)\n3: day(d)\n4: hour(d)\n5: second(s) ::")
elif userInput01 == 's':
    userInput02 = input("Convert second yo..\n1: year(y)\n2: month(m)\n3: day(d)\n4: hour(d)\n5: minute(M) :")
else:
    print("not founded..")
userInput02.lower()

def show(x,y):
    userNumber=int(input(f"Please enter the number of {x} you wish to convert into {y} :"))
    return userNumber

if userInput01=='y':
    if userInput02=='m':
        userNumber = show('year','month')
    elif userInput02=='d':
        userNumber = show('year', 'day')
    elif userInput02=='h':
        userNumber = show('year', 'hour')
    elif userInput02=='M':
        userNumber = show('year', 'minute')
    elif userInput02=='s':
        userNumber = show('year', 'second')
elif userInput01=="m":
    if userInput02=='y':
        userNumber = show('month','year')
    elif userInput02=='d':
        userNumber = show('month', 'day')
    elif userInput02=='h':
        userNumber = show('month', 'hour')
    elif userInput02=='M':
        userNumber = show('month', 'minute')
    elif userInput02=='s':
        userNumber = show('month', 'second')
elif userInput01=="d":
    if userInput02=='y':
        userNumber = show('day','year')
    elif userInput02=='m':
        userNumber = show('day', 'month')
    elif userInput02=='h':
        userNumber = show('day', 'hour')
    elif userInput02=='M':
        userNumber = show('day', 'minute')
    elif userInput02=='s':
        userNumber = show('day', 'second')
elif userInput01=="h":
    if userInput02=='y':
        userNumber = show('hour','year')
    elif userInput02=='m':
        userNumber = show('hour', 'month')
    elif userInput02=='d':
        userNumber = show('hour', 'day')
    elif userInput02=='M':
        userNumber = show('hour', 'minute')
    elif userInput02=='s':
        userNumber = show('hour', 'second')
elif userInput01=="M":
    if userInput02=='y':
        userNumber = show('minute','year')
    elif userInput02=='m':
        userNumber = show('minute', 'month')
    elif userInput02=='d':
        userNumber = show('minute', 'day')
    elif userInput02=='h':
        userNumber = show('minute','hour')
    elif userInput02=='s':
        userNumber = show('minute', 'second')
elif userInput01=="s":
    if userInput02=='y':
        userNumber = show('second','year')
    elif userInput02=='m':
        userNumber = show('second', 'month')
    elif userInput02=='d':
        userNumber = show('second', 'day')
    elif userInput02=='h':
        userNumber = show('second','hour')
    elif userInput02=='M':
        userNumber = show('second', 'minute')

def year():
    if userInput02 == "m":
        print(f"It is {userNumber} year,{userNumber*12} months.")
    elif userInput02 == "d":
        print(f"It is {userNumber} year,{userNumber*365} days.")
    elif userInput02 == "h":
        print(f"It is {userNumber} year,{userNumber*365*24+(userNumber*6)} hours.(365 days and 6 hours every year)")
    elif userInput02 == "M":
        print(f"It is {userNumber} year,{(userNumber*365*24+(userNumber*6))*60} minutes.")
    elif userInput02 == "s":
        print(f"It is {userNumber} year,{(userNumber*365*24+(userNumber*6))*60*60} seconds.")
    else :
        print("not found.")

def month():
    if userInput02 == "y":
        print(f"It is {userNumber} month,{userNumber/12} years.")
    elif userInput02 == "d":
        print(f"It is {userNumber} month,{userNumber*30} days.")
    elif userInput02 == "h":
        print(f"It is {userNumber} month,{userNumber*30*24} hours.")
    elif userInput02 == "M":
        print(f"It is {userNumber} month,{userNumber*30*24*60} minutes.")
    elif userInput02 == "s":
        print(f"It is {userNumber} month,{userNumber*30*24*60*60} seconds.")
    else:
        print("not found..")

def day():
    if userInput02 == "y":
        print(f"It is {userNumber} day,{userNumber/365} years.")
    elif userInput02 == "m":
        print(f"It is {userNumber} day,{userNumber/30} months.")
    elif userInput02 == "h":
        print(f"It is {userNumber} day,{userNumber*24} hours.")
    elif userInput02 == "M":
        print(f"It is {userNumber} day,{userNumber*24*60} minutes.")
    elif userInput02 == "s":
        print(f"It is {userNumber} day,{userNumber*24*60*60} seconds.")
    else:
        print("not found...")

def hour():
    if userInput02 == "y":
        print(f"It is {userNumber} hour,{userNumber/(24*365)} years.")
    elif userInput02 == "m":
        print(f"It is {userNumber} hour,{userNumber/(24*30)} months.")
    elif userInput02 == "d":
        print(f"It is {userNumber} hour,{userNumber/24} days.")
    elif userInput02 == "M":
        print(f"It is {userNumber} hour,{userNumber*60} minutes.")
    elif userInput02 == "s":
        print(f"It is {userNumber} hour,{userNumber*60*60} seconds.")
    else:
        print("not found....")

def minute():
    if userInput02 == "y":
        print(f"It is {userNumber} minute,{userNumber/(60*24*365)} years.")
    elif userInput02 == "m":
        print(f"It is {userNumber} minute,{userNumber/(60*24*30)} months.")
    elif userInput02 == "d":
        print(f"It is {userNumber} minute,{userNumber/(60*24)} days.")
    elif userInput02 == "h":
        print(f"It is {userNumber} minute,{userNumber/60} hours.")
    elif userInput02 == "s":
        print(f"It is {userNumber} minute,{userNumber*60} seconds.")
    else:
        print("not found.....")

def second():
    if userInput02 == "y":
        print(f"It is {userNumber} seconds,{userNumber/(60*60*24*365)} years.")
    elif userInput02 == "m":
        print(f"It is {userNumber} seconds,{userNumber/(60*60*24*30)} months.")
    elif userInput02 == "d":
        print(f"It is {userNumber} seconds,{userNumber/(60*60*24)} days.")
    elif userInput02 == "h":
        print(f"It is {userNumber} seconds,{userNumber/(60*60)} hours.")
    elif userInput02 == "M":
        print(f"It is {userNumber} seconds,{userNumber/60} minutes.")
    else:
        print("not found......")

def run():
    if userInput01 == 'y':
        year()
    elif userInput01 == 'm':
        month()
    elif userInput01 == 'd':
        day()
    elif userInput01 == 'h':
        hour()
    elif userInput01 == 'M':
        minute()
    elif userInput01 == 's':
        second()
    else:
        print('not found.................')

if __name__ == "__main__":
    run()
