from re import A
from tkinter import W


age = input("What is your age?\n")
a=int(age)
y=90-a
d=y*365
w=y*52
m=y*12
print(f"You have {d} days, {w} weeks and {m} months left to be alive if you live upto 90 years of age.")