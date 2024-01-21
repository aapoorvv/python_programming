from tkinter import *

window = Tk()
window.title("hehehe")
window.minsize(500,500)
#label
my_label = Label(text="huehuehuehue Label",font=("Arial",20,"bold"))
my_label.pack(side="bottom",expand=0)

# my_label.config(text="new text")

#button
def button_clicked():
    print("clicked bitches")
    # my_label["text"] = "new text"
    #or
    # my_label.config(text="clicked bitches")
    my_label.config(text=input.get())
    
button = Button(text = "click me", command=button_clicked)
button.pack()


input = Entry()
input.pack()












window.mainloop()