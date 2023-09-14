import random
import os
from art import logo

def check(g,a):
    if g<a:
        return 1
    elif g>a:
        return 2
    else:
        return 0
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
# print(f"Pssst, the correct answer is {answer}")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if choice == "easy":
    n = 10
else:
    n = 5
print(f"\nYou have {n} attempts to guess the number.")
while n != 0:
    guess = int(input("\nMake a guess: "))
    x = check(guess,answer)
    n-=1
    if x==1:
        print(f"{guess} is too low.")
        if n>0:
            print("Guess again.")
            print(f"You have {n} attempts remaining to guess the number.")
    elif x == 2:
        print(f"{guess} is too high.")
        if n>0:
            print("Guess again.")
            print(f"You have {n} attempts remaining to guess the number.")
    else: 
        print(f"\nYou got it! The answer was {answer}.")
        break
if x!=0:
    print(f"\nYou've run out of guesses, you lose. The answer was {answer}.")