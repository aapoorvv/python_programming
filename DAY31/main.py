from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(new_data)
    canvas.itemconfig(card_image,image=front_img)
    canvas.itemconfig(card_title,text="French",fill="Black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="Black")
    flip_timer = window.after(3000,func = flip_card)
    
def flip_card():
    canvas.itemconfig(card_image,image=back_img)
    canvas.itemconfig(card_title,text="English",fill="White")
    canvas.itemconfig(card_word,text=current_card["English"],fill="White")
    
def learned():
    new_data.remove(current_card) 
    data = pd.DataFrame(to_learn)
    data.to_csv ("DAY31/data/words_to_learn.csv")
    next_card()
    
window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func = flip_card)

current_card = {}
data = pd.read_csv("DAY31/data/french_words.csv")
new_data = data.to_dict(orient="records")



canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="DAY31/images/card_front.png")
back_img = PhotoImage(file="DAY31/images/card_back.png")
card_image = canvas.create_image(400,263,image = front_img)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"),fill="black")
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"),fill="black")
canvas.grid(row= 0,column=1,columnspan=2)

cross_img = PhotoImage(file="DAY31/images/wrong.png")
cross = Button(image=cross_img,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=next_card)
cross.grid(row=2,column=1)

tick_img = PhotoImage(file="DAY31/images/right.png")
tick = Button(image=tick_img,highlightthickness=0, highlightbackground=BACKGROUND_COLOR,command=learned)
tick.grid(row=2,column=2)

next_card()

window.mainloop()