import turtle
turtle.shape('turtle')
turtle.speed(10)
def  circle(n):
    for i in range(360):
        turtle.speed(10)
        turtle.forward(n)
        turtle.right(1)
turtle.penup()
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
circle(2)
turtle.end_fill()
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
circle(0.3)
turtle.end_fill()
turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
circle(0.3)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.fillcolor('black')
turtle.right(90)
turtle.width(5)
turtle.forward(50)
turtle.penup()
turtle.goto(-55, -150)
turtle.pendown()
turtle.fillcolor('red')
def duga():
    for i in range(180):
        turtle.speed(10)
        turtle.pencolor('red')
        turtle.forward(1)
        turtle.left(1)
duga()

