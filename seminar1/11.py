import turtle
turtle.shape('turtle')
turtle.speed(10)
def circle(n):
    for i in range(360):
        turtle.speed(10)
        turtle.forward(n/5)
        turtle.left(1)
turtle.right(90)
for i in range(1, 5):
    for j in range(1, 3):
        circle(i)
        turtle.right(180)
