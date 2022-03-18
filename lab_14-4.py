import turtle

# setting window dimensions
window = turtle.Screen()
window.setup()
window.screensize()
window.title("LAB 4")
#setiing turtle specifications
turtle1 = turtle.Turtle()
turtle1.shape('turtle')
turtle1.color('Green')
turtle1.speed(3)
turtle1.setposition(100, 100)
turtle1.stamp()
#for loop to make equilateral triangle
turtle1.begin_fill()
for number in range(3):
    turtle1.forward(200)
    turtle1.left(90)
turtle1.end_fill()
window.mainloop()