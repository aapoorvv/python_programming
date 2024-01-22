from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

RED = "#EF5C53"

# FIND PASSWORD -------------------------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("DAY29/data.json", "r") as data_file:
            #Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="Error:\nNo data file found.")
    else:
        if website in data:
            messagebox.showinfo(title=website,message=f"Username: {data[website]['username']}\nPassword: {data[website]['password']}")
            pyperclip.copy(data[website]['password'])
        else:
            messagebox.showinfo(title="Error",message="Error:\nNo details for this website exists.")

# PASSWORD GENERATOR -------------------------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers= [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0,password)

# SAVE PASSWORD -------------------------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password =password_input.get()
    new_data={
        website: {
            "username": username,
            "password": password
        }
    }
    if len(website)==0 or len(password)==0 or len(username)==0:
        messagebox.showinfo(title='oops',message="Please make sure you haven't left any field(s) empty.")
        return
    
    is_okay = messagebox.askokcancel(title=website,message=f"Confirm the following: \nUsername: {username}\nPassword: {password}\n Save?")
    if is_okay:
        # # working with .txt file
        # with open("DAY29/data.txt","a") as file:
        #     file.write(f"{website} | {username} | {password}\n")
        #     file.close
        # website_input.delete(0,END)
        # password_input.delete(0,END)
        try:
            with open("DAY29/data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("DAY29/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:  
            #Updating old data with new data     
            data.update(new_data)
            with open("DAY29/data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally: 
            website_input.delete(0,END)
            password_input.delete(0,END)
            
# UI SETUP -------------------------------------------------- #

window = Tk()
window.title("MY PASS")
window.config(padx=50,pady=50 )

# website row
website_label = Label(text="Website:     ",  fg=RED,font=("Segoe UI",13,"bold"))
website_label.grid(row=1,column=0)

website_input = Entry(width="21",borderwidth=1)
website_input.grid(row=1,column=1)
website_input.focus()

search_button = Button(text="Search",width=10,bg="blue",fg="blue",font=("Segoe UI",13,"bold"),command=find_password)
search_button.grid(row=1,column=2)

# username row
username_label = Label(text="Username/Email:   ", fg=RED,font=("Segoe UI",13,"bold"))
username_label.grid(row=2,column=0)

username_input = Entry(width="35",borderwidth=1)
username_input.grid(row=2,column=1,columnspan=2)
username_input.insert(0,"abc@gmail.com")

# password row
password_label = Label(text="Password:   ",  fg=RED,font=("Segoe UI",13,"bold"))
password_label.grid(row=3,column=0)

password_input = Entry(width="21",borderwidth=1)
password_input.grid(row=3,column=1)

generate_button = Button(text="Generate",width=10,command=generate_password,fg="#f79f07",font=("Segoe UI",13,"bold"))
generate_button.grid(row=3,column=2)
   
# add button row
add_button = Button(text="Add",width=33,command=save,fg="green",font=("Segoe UI",13,"bold"))
add_button.grid(row=4,column=1,columnspan=2)


canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="DAY29/logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(row= 0,column=1)



window.mainloop()