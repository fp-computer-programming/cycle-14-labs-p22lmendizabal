# author: LM (AMDG) 3/21/22
import turtle
# creating window
window = turtle.Screen()
window.screensize(1000,1000)
window.title("Lab 6")
# creating turtle
turtle1 = turtle.Turtle()

# function that draws square with color and shape by user
def when_click():
    turtle1.color(turtle.textinput("color", "what color do you want?"))
    turtle1.shapesize(turtle.numinput("size", "What size do you want drom 1 to 5? ", default=None, minval=1, maxval=5))
    # fills in color
    turtle1.begin_fill()
    # draws square
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(100)
    # ends
    turtle1.end_fill()
    return
    
when_click()
window.mainloop()