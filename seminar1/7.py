import turtle
turtle.shape('turtle')
count=0
a=0.1
for i in range(360*10):
    turtle.speed(10)
    turtle.forward(a)
    turtle.left(1)
    count+=1
    if count%200==0:
        a+=0.1
