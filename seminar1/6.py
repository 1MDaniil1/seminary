import turtle
n=int(input())
turtle.shape('turtle')
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.goto(0,0)
    turtle.right(360/n)
