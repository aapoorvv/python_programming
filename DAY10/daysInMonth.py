def leap(y):
    """To check if a year is a leap or not"""
    l = "non leap"
    if y%4==0:
        l = "leap"
        if y%100==0:
            l = "non leap"
            if y%400==0:
                l = "leap"
    return l

def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(leap(year) == "leap"):
        month_days[1]=29
    return month_days[month-1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(f"No. of days in month {month} of year {year} is",days)