# author: LM (AMDG) 3/17/22
import turtle
#craeting scrren and screen size
window = turtle.Screen()
window.screensize(500,500)
window.title("Lab 2")
window.setup(1000,1000)
# creating turtle and giving it directions to make equilateral triangle
turtle1 = turtle.Turtle()
turtle1.right(45)
turtle1.forward(100)
turtle1.right(135)
turtle1.forward(100)
turtle1.right(135)
turtle1.forward(100)
#making sure window does not close
window.mainloop()