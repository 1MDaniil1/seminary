from random import randint, uniform
import turtle

number_of_turtles = 40
steps_of_time_number = 500

turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
turtle.penup()
turtle.goto(-250, -250)
turtle.pendown()
turtle.goto(-250, 250)
turtle.goto(250, 250)
turtle.goto(250, -250)
turtle.goto(-250, -250)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.shapesize(0.5, 0.5)
    unit.vx = uniform(-1, 1) * 3
    unit.vy = uniform(-1, 1) * 3
    unit.penup()
    unit.speed(100)
    unit.goto(randint(-200, 200), randint(-200, 200))

for i in range(steps_of_time_number):
    for unit in pool:
        x = unit.xcor() + unit.vx
        y = unit.ycor() + unit.vy
        unit.goto(x, y)
        if unit.xcor() <= -250:
            unit.vx = -unit.vx
        if unit.ycor() <= -250:
            unit.vy = -unit.vy
        if unit.xcor() >= 250:
            unit.vx = -unit.vx
        if unit.ycor() >= 250:
            unit.vy = -unit.vy
