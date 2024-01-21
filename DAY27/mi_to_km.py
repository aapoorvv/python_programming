from tkinter import *

window = Tk()
window.title("Miles to Kilometres Converter")
window.minsize(120,80)

input = Entry(width="9")
input.grid(row=1,column=1)

mi_label = Label(text="miles")
mi_label.grid(row=1,column=2)

isequal_label = Label(text="is equal to")
isequal_label.grid(row=2,column=0)

res_label = Label(text=" 0 ")
res_label.grid(row=2,column=1)

km_label = Label(text=" Kms ")
km_label.grid(row=2,column=2)

def calculate():
    mi=float(input.get())
    km = mi*1.609
    res_label.config(text=f" {km} ")

button = Button(text = "calculate", command=calculate)
button.grid(row=3,column=1)

window.mainloop()