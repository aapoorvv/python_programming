import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names[random.randint(0,len(names)-1)])
