import turtle
a=100
for i in range(10):
    turtle.shape('turtle')
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.penup()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(180)
    turtle.pendown()
    a+=40
   
