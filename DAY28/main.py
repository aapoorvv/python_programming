from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#259c1f"
YELLOW = "#F9F9C5"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer",fg="black")
    tick_label.config(text="")
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps%2==1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps%8==0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    a,b='',''
    if count%60<10:
        b='0'
    if count/60<10:
        a='0'
        # canvas.itemconfig(timer_text,text =f"{int(count/60)}:0{count%60}")
    canvas.itemconfig(timer_text,text =f"{a}{int(count/60)}:{b}{int(count%60)}")
    if count>0:
        global my_timer 
        my_timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        global reps
        ticks=""
        work_sets = int(reps/2)
        for _ in range(work_sets):
            ticks += "✓" 
        tick_label.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer_label = Label(text="TIMER",bg=YELLOW,fg="black",font=(FONT_NAME,35,"bold"))
timer_label.grid(row=1,column=2)

canvas = Canvas(width=230,height=230,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="DAY28/tomato.png")
canvas.create_image(115,115,image = tomato_img)
timer_text = canvas.create_text(115,130,text="00:00",fill=YELLOW,font=("Courier",35,"bold"))
canvas.grid(row=2,column=2)


start = Button(text="START",highlightbackground=YELLOW,fg=GREEN,font=(FONT_NAME,25,"bold"),command=start_timer)
start.grid(row=3,column=1)

tick_label = Label(text="",bg=YELLOW,font=(FONT_NAME,25,"bold"),fg="black")
tick_label.grid(row=4,column=2)

reset = Button(text="RESET",highlightbackground=YELLOW,fg=GREEN,font=(FONT_NAME,25,"bold"),command=reset_timer)
reset.grid(row=3,column=3)




window.mainloop()