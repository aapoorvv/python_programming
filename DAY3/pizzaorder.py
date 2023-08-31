print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
b = 0
if size == 'S' or size =='s':
    b += 15
elif size == 'M' or size =='m':
    b += 20
else :
    b += 25
if add_pepperoni == 'Y' or add_pepperoni ==  'y':
    if size == 'S' or size == 's':
        b+=2
    else:
        b+=3
if extra_cheese == 'Y' or extra_cheese == 'y':
    b+=1
print(f"Your total bill is {b}$.")