import turtle
import math

turtle.shape('turtle')

def polygon(n, a):
    turtle.goto(0, 0)
    r = a / (2 * math.sin((math.pi)/n))
    turtle.penup()
    turtle.forward(r)
    turtle.pendown()
    turtle.left(90 + (180 / n))
    for i in range(0,n):
        turtle.forward(a)
        turtle.left(360/n)
    turtle.right(90 + (180 / n))
    turtle.penup()
a = 10
for j in range(3, 13):
    polygon(j, a)
    a = a + 10

    
