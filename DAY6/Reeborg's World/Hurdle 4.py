def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    if front_is_clear():
        move()
    else:
        turn_left()
    if right_is_clear():
        turn_right()
    while front_is_clear():
        move()
    if wall_in_front():
        turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
