from calendar import leapdays


y = int(input("Which year do you want to check? "))
l = "non leap"

if y%4==0:
    l = "leap"
    if y%100==0:
        l = "non leap"
        if y%400==0:
            l = "leap" 
print(f"Year {y} is a {l} year.")
    
    