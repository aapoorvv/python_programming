h=float(input("Enter your height(in cm): "))
w=float(input("Enter your weight(in kgs): "))
b=(w/h**2)*10000
print("Your BMI =","%.2f"%(b))
if b<18.5:
    print("You're underweight.")
elif 18.5<=b<=25:
    print("You're normal weight.")
elif 25<b<=30:
    print("You're overweight.")
elif 30<b<35:
    print("You're obese.")
else:
    print("You're clinically obese.")

