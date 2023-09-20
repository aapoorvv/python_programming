import random
import os
from game_data import data
from art import logo,vs
score = 0
def check(ans,a,b):
    if ans == 'A': 
        if a['follower_count']>= b['follower_count']:
            return True
        else:
            return False
    if ans == 'B': 
        if a['follower_count']<= b['follower_count']:
            return True
        else:
            return False
        
a = data[random.randint(0,len(data)-1)]
while True:
    b = data[random.randint(0,len(data)-1)]
    while a==b:
        b = data[random.randint(0,len(data)-1)]   
    print(logo)
    print(f"\nCompare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")
    ans = input("\nWho has more followers? Type 'A' or 'B': ")
    res = check(ans,a,b)
    a = b
    os.system('clear')
    if res:
        score+=1
        print(f"You're right! Current score: {score}.\n")
    else:
        print(f"\nSorry, that's wrong. Final score: {score}.\n")
        break
    