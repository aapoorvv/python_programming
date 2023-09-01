import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
img = [rock, paper, scissors]
a = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors : "))
b = random.randint(0,2)
c = "You lose."
if(a==b):
    c = "It's a draw."
elif(a==0 and b==2):
    c ="You won."
elif(a==1 and b==0):
    c="You won."
elif(a==2 and b==1):
    c="You won."
print("You:",img[a],"\nComputer:",img[b])
print(c)
