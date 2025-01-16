import turtle
import random
d=turtle.Turtle()
def tur():
    d=turtle.Turtle()
    turtle.clearscreen()
    d.shape("turtle")
    turtle.bgcolor("black")
    turtle.colormode(255)
    turtle.colormode(255)
def desings():
    return random.randint(0,255)
tur()  
side=5 

d.speed("fastest")
for q in range(1000):
    x=desings()
    y=desings()
    z=desings()
    d.pencolor(x,y,z)
    d.forward(side)
    d.right(91)
    side=side+1
d.goto(0,0)
tur()  
side=5 
for q in range(1000):
    x=desings()
    y=desings()
    z=desings()
    d.pencolor(x,y,z)
    d.forward(side)
    d.right(61)
    side=side+1
d.goto(0,0)
tur()  
side=5 
for q in range(900):
    x=desings()
    y=desings()
    z=desings()
    d.pencolor(x,y,z)
    d.circle(side)
    d.right(91)
    side=side+1
d.goto(0,0)
tur()  
side=5 
for q in range(1000):
    x=desings()
    y=desings()
    z=desings()
    d.pencolor(x,y,z)
    d.forward(side)
    d.right(73)
    side=side+1

d.goto(0,0)
tur()  
side=5 
for q in range(1000):
    x=desings()
    y=desings()
    z=desings()
    d.pencolor(x,y,z)
    d.forward(side)
    d.right(61)
    side=side+1
    d.right(61)
    side=side+1
    d.right(61)
    side=side+1