import turtle
import numpy as np
turtle.shape('circle')
turtle.shapesize(0.5)
turtle.speed(10)
g=10
vx=50
vy=100
x=0
y=0
count=0
k=0.005
for i in range(1000):
    if y<=0:
        vy=abs(vy)
        count+=1
    vx-=k*vx
    vy-=k*vy
    x+=vx*i/5000
    y+=vy*i/5000-g*((i/5000)**2)/2
    turtle.goto(x, y)
    vy-=g*i/5000
