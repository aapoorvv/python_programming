import  datetime as dt

now = dt.datetime.now()
print(now.second)
print(now.weekday())
print(now.microsecond)

dob = dt.datetime(year = 2002, month = 9, day =26)
print(dob)