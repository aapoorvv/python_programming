from turtle import Turtle
from turtle import Screen
import pandas as pd

t = Turtle()
t.penup()
t.hideturtle()
screen = Screen()
screen.title("US States")
image = "DAY25.3/blank_states_img.gif"
screen.addshape(image)
screen.bgpic(image)

# def get_mouse_click_coor(x,y) :
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pd.read_csv("DAY25.3/50_states.csv")
states = (data["state"])
score = 0
guessed_states = []
while score<=50:
    answer_state = screen.textinput(f"{score}/50 States Done","What's another states name?")
    if answer_state == "Exit":
    #     missing_states = []
    #     for state in states:
    #         if state not in guessed_states:
    #             missing_states.append(state)
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("DAY25.3/missed_states.csv")
        break
    for state in states:
        if answer_state==state:
            score+=1
            s= data[data.state == state]
            t.setpos(int(s.x),int(s.y))
            t.write(state,font=("Monotype", 13, "normal"))
            guessed_states.append(state)
        if score==50:
            t.goto(-250,0)
            t.write("CONGRATULATIONS",font=("Monotype", 50, "normal"))
            
