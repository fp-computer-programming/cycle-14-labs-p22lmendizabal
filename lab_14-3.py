#author: LM (AMDG) 3/18/22
import turtle
# setting window dimensions
window = turtle.Screen()
window.screensize(500, 500)
window.title("LAB 3")
#setiing turtle specifications
turtle1 = turtle.Turtle()
turtle1.shape('turtle')
turtle1.pencolor('Green')
#for loop to make equilateral triangle
for number in range(3):
    turtle1.left(135)
    turtle1.forward(200)
window.mainloop()