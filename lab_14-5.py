# author: LM (AMDG) 3/21/22
from curses import window
import turtle
# creating window 
window = turtle.Screen()
window.screensize(1000, 1000)
window.title("Lab 5")

# creating turtle
turtle1 = turtle.Turtle()

# function for moving the turtle
def move_forward():
    turtle1.forward(10)

def move_backward():
    turtle1.back(10)

def turn_left():
    turtle1.left(90)

def turn_right():
    turtle1.right(90)

#calling function and associating it with a key
window.onkey(move_forward,"Up")
# backawrds = down key
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")
# senses keyb being clicked
window.listen()
window.mainloop()
