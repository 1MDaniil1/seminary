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
l=[s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
with open('2.txt', 'w') as f:
    f.writelines(str(l))
with open('2.txt', 'r') as f:
    a=eval(f.read())
def digit(s):
    if s==1:
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    if s==2 or s==3 or s==4 or s==7:
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
    for i in a[s]:
        turtle.forward(i[0])
        turtle.right(i[1])
    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()
    f=0
    for j in a[s]:
        f+=j[1]
    turtle.left(f)
x=70
for i in 1, 4, 1, 7, 0, 0:
    digit(i)
    x+=70

