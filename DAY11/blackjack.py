from art import logo
import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

user_cards = []
dealer_cards = []

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,dealer_score,choice):
    if user_score == dealer_score == 0:
        print("\nIt's a Draw")
        return False
    elif dealer_score == 0:
        print("\nDealer's Blackjack. You Lose.")
        return False
    elif user_score == 0:
        print("\nUser's Blackjack. You Win.")
        return False
    elif user_score > 21:
        print("\nUser Bust. You Lose.")
        return False
    elif dealer_score >21:
        print("\nDealer Bust. You Win.")
        return False
    elif choice == 's':
        if user_score > dealer_score:
            print("\nYou Win.")
        elif  user_score < dealer_score:  
            print("\nYou Lose.")
        else:
            print("\nIt's a Draw")
        return False
    else:
        return True
isGameOver = True
for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
choice = 'h'
while isGameOver:   
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    os.system('clear')
    print(logo)
    print("Your score: ", user_score)
    print("Your hand: ",user_cards)
    print("Dealer first card: " ,dealer_cards[0])
    isGameOver = compare(user_score,dealer_score,choice)
    if isGameOver == False:
        print(f"\nYour final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {dealer_cards}, final score:{dealer_score}")
        break
    choice = input("Do you want to hit or stand? h or s: ")
    if choice == 'h':
        user_cards.append(deal_card())
    while 0<calculate_score(dealer_cards)<17:
        dealer_cards.append(deal_card())