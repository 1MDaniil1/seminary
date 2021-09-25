import turtle
turtle.shape('turtle')
turtle.speed(10)
turtle.left(180)
def zvezda(n):
    for i in range(n):
        turtle.forward(100)
        turtle.left(180-180/n)
zvezda(5)
turtle.penup()
turtle.goto(200,0)
turtle.pendown()
zvezda(11)
