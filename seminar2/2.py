import turtle
import numpy as np
turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
s0=[(100, 90), (40, 90), (100, 90), (40, 0)]
s1=[(0, 45), (np.sqrt(2)*50, 135), (100, 0)]
s2=[(0, 90), (50, 90), (50, 45), (np.sqrt(2)*50, 225), [50, 0]]
s3=[(0, 90), (50, 135), (np.sqrt(2)*50, 225), (50, 135), (np.sqrt(2)*50, 0)]
s4=[(0, 180), (50, 270), (50, 270), (50, 180), (100, 0)]
s5=[(0, 90), (50, 270), (50, 270), (50, 90), (50, 90), (50, 0)]
s6=[(50, 90), (50, 90), (50, 90), (50, 90), (50, 45), (np.sqrt(2)*50, 0)]
s7=[(0, 90), (50, 135), (np.sqrt(2)*50,315), (50, 0)]
s8=[(100, 90), (50, 90), (100, 90), (50, 90), (50, 90), (50, 0)]
s9=[(0, 45), (np.sqrt(2)*50, 315), (50, 270), (50, 270), (50, 270), (50, 0)]
def digit(s):
    if s==s1:
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    if s==s2 or s==s3 or s==s4 or s==s7:
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
    for i in s:
        turtle.forward(i[0])
        turtle.right(i[1])
    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()
    f=0
    for j in s:
        f+=j[1]
    turtle.left(f)
x=70
for i in s1, s4, s1, s7, s0, s0:
    digit(i)
    x+=70


