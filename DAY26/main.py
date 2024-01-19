#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd

A = pd.read_csv("DAY26/nato_phonetic_alphabet.csv")
B = {row.letter:row.code for index,row in A.iterrows()}
# print(B)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def func():
    word = (input("Enter a word: ")).upper()
    try:  
        li = [B[letter] for letter in word]
    except KeyError:
        print("please enter a valid word.")
        func()
    else: 
        print(li)
        return 

func()