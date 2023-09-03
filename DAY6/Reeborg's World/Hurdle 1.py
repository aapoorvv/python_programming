def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

for i in range(0,6):
        move()
        jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
