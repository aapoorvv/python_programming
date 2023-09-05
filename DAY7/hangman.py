import random
import os
from hangman_art import stages
from hangman_art import logo
print(logo+"\n")

from hangman_words import word_list
chosen_word = random.choice(word_list)
display = []
for i in chosen_word:
    display.append("_")
end = False
lives = 6
while not end:    
    guess = input("\nGuess a letter: ").lower()
    os.system('clear')
    a = 0
    print(logo+"\n")
    print(f"Last letter: {guess}")
    if guess in display:
        print(f"You've already guessed letter '{guess}'.")
    for letter in chosen_word:
        if guess == letter:
            c = chosen_word.index(guess,a)
            a = c+1
            display[c] = guess
    print()
    if a == 0:
        lives-=1
    for i in display:
        print (i,end=" ")
    # **** other method for above for loop ****
    # for position in range(word_length):
    #     letter = chosen_word[position]
    #     #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    #     if letter == guess:
    #         display[position] = letter
    print("\n",stages[lives])
    print("Lives :",lives)
    if "_" not in display:
        end = True
        print(f"\nYou won.\nYou guessed it right, it's {chosen_word}.\n")
    if lives == 0:
        end = True
        print('''\nYou lose.''')
        print(f"\nThe word was {chosen_word}.\n")
        