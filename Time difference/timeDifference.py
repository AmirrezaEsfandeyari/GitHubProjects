
print("a program for convert time.!!\nPlease Enter the date as {2000/01/01}!!")
day_1=int(input("Please enter the first date day :"))
month_1=int(input("Please enter the first date month :"))
year_1=int(input("Please enter the first date year :"))

print(f"your enter date =>{year_1}/{month_1}/{day_1}.")

day_2=int(input("Please enter the second date day :"))
month_2=int(input("Please enter the second date month :"))
year_2=int(input("Please enter the second date year :"))

print(f"your enter date =>{year_2}/{month_2}/{day_2}.")
def date(month_1=month_1,year_1=year_1,month_2=month_2, year_2=year_2):
    if year_2 > year_1:
        if month_2 > month_1:
            if day_2 > day_1:
                day = day_2 - day_1
                month=month_2-month_1
                year=year_2-year_1
                #return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                    f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            elif day_2 == day_1:
                day = 0
                month = month_2 - month_1
                year = year_2 - year_1
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            else:
                month_2-= 1
                day = (day_2 + 30) - day_1
                month = month_2 - month_1
                year = year_2 - year_1
                #return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
        elif month_2==month_1:
            if day_2 > day_1:
                day = day_2 - day_1
                month=0
                year = year_2 - year_1
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
                #return day,month,year
            elif day_2 == day_1:
                day = 0
                month = 0
                year = year_2 - year_1
                #return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            else:
                year_2-=1
                month_2+=12
                month_2-= 1
                day = (day_2 + 30) - day_1
                month=month_2 - month_1
                year=year_2-year_1
                #return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
        else:#monyh2<month1
            if day_2 > day_1:
                day = day_2 - day_1
                year_2 -= 1
                month = (month_2 + 12) - month_1
                year = year_2 - year_1
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            elif day_2 == day_1:
                day = 0
                year_2 -= 1
                month = (month_2 + 12) - month_1
                year = year_2 - year_1
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            else:
                if month_2>1:
                    month_2 -= 1
                    day = (day_2 + 30) - day_1
                    year_2 -= 1
                    month = (month_2 + 12) - month_1
                    year = year_2 - year_1
                    # return day,month,year
                    print(f"there is {day} day,{month} month and {year} year between the dates."
                          f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
                else:
                    year_2 -= 1
                    month_2 += 12
                    month_2 -= 1
                    day = (day_2 + 30) - day_1
                    month = month_2  - month_1
                    year = year_2 - year_1
                    # return day,month,year
                    print(f"there is {day} day,{month} month and {year} year between the dates."
                          f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
    elif year_2==year_1:
        if month_2 > month_1:
            if day_2 > day_1:
                day = day_2 - day_1
                month = month_2 - month_1
                year=0
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            elif day_2 == day_1:
                day=0
                month = month_2 - month_1
                year = 0
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            else:
                month_2 -= 1
                day = (day_2 + 30) - day_1
                month = month_2 - month_1
                year = 0
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
        elif month_2 == month_1:
            if day_2 > day_1:
                day = day_2 - day_1
                month=0
                year = 0
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            elif day_2 == day_1:
                day = 0
                month = 0
                year = 0
                # return day,month,year
                #return 0
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            else:#day2<day1
                day = day_1  - day_2
                month = 0
                year = 0
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
        else:  # month2<month1
            if day_2 > day_1:
                month_1-=1
                day = (day_1+30)- day_2
                month = month_1 - month_2
                year=0
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            elif day_2 == day_1:
                day = 0
                month = month_1 - month_2
                year = 0
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            else:
                day = day_1 - day_2
                month = month_1 - month_2
                year = 0
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
    else:#year_2 < year_1
        if month_1 > month_2:
            if day_1 > day_2:
                day = day_1 - day_2
                month = month_1 - month_2
                year = year_1 - year_2
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            elif day_1 == day_2:
                day = 0
                month = month_1 - month_2
                year = year_1 - year_2
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            else:
                month_1-= 1
                day = (day_1 + 30) - day_2
                month = month_1 - month_2
                year = year_1 - year_2
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
        elif month_2==month_1:
            if day_1 > day_2:
                day = day_1 - day_2
                month=0
                year = year_1 - year_2
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            elif day_1 == day_2:
                day = 0
                month = 0
                year = year_1 - year_2
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            else:
                year_1-=1
                month_1+=12
                month_1-= 1
                day = (day_1 + 30) - day_2
                month=month_1-month_2
                year = year_1 - year_2
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
        else:#monyh2>month1
            if day_1 > day_2:
                day = day_1 - day_2
                year_1 -= 1
                month = (month_1 + 12) - month_2
                year = year_1 - year_2
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            elif day_1 == day_2:
                day = 0
                year_1 -= 1
                month = (month_1 + 12) - month_2
                year = year_1 - year_2
                # return day,month,year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")
            else:
                # if month_1>1:
                #     month_1 -= 1
                #     day = (day_1 + 30) - day_2
                #     return day
                # else:
                #     year_1 -= 1
                #     month_1 += 12
                #     month_1 -= 1
                #     day = (day_1 + 30) - day_2
                #     return day
                year_1-=1
                month_1+=12
                month_1-=1
                day = (day_1+30) - day_2
                month=month_1-month_2
                year = year_1 - year_2
                # return day, month, year
                print(f"there is {day} day,{month} month and {year} year between the dates."
                      f"\n(date1={year_1}/{month_1}/{day_1} and date2={year_2}/{month_2}/{day_2})")


date()