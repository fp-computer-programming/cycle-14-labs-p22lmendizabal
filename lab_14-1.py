#author: LM (AMDG) 3/17/22
# importing turtle
import turtle
#creating window and screensize
window = turtle.Screen()
window.setup(1000, 1000)
window.screensize(900, 600)
window.title("Lab 1")
#makinf first turtle And giving directions
turtle1 = turtle.Turtle()
turtle1.forward(250)
turtle1.left(90)
turtle1.forward(100)
turtle1.left(90)
turtle1.forward(250)
turtle1.left(90)
turtle1.forward(100)
#making sure window does not close
window.mainloop()