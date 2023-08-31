print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
n = name.lower()
t = n.count('t')
r = n.count('r')
u = n.count('u')
e = n.count('e')
l = n.count('l')
o = n.count('o')
v = n.count('v')
u = n.count('e')
true = t+r+u+e
love = l+o+v+u
st = str(true) + str(love)
s = int(st)
if s>=90 or s<=10:
    print(f"Your score is {s}, you go together like coke and mentos.")
elif 40<=s<=50:
    print(f"Your score is {s}, you both go alright together.")
else:
    print(f"Your score is {s}")