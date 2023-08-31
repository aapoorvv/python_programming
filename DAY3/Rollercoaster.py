print("Welcome to the Rollercoaster!")
h = int(input("What is your height in cm? "))
b = 0
if h>120:
    print("You can ride the rollercoaster. ")
    a = int(input("What is your Age? "))
    if a<12:
        b = 5
    elif 12<=a<18:
        b =7
    elif 45<=a<=55 :
        print("You can have a free ride on us!")
        b = 0
    else:
        b = 9
    photo = input("Do you want a photo taken? (for 3$ only) Y/N: ")
    if photo == 'Y' or photo == 'y':
        b+=3
    print(f"You have to pay {b}$.")
else:
    print("Sorry, You cannot ride the rollercoaster.")