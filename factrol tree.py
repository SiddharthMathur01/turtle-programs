import turtle
import random

turtle.bgcolor("black")
turtle.colormode(255)
t=turtle.Turtle()
t.shape("turtle")
t.pencolor("white")
t.setheading(90)
t.pensize(2)
t.speed("fastest")
t.hideturtle()
t.penup()
t.goto(0,-250)
t.pendown()
ang=20


def desings():
    return random.randint(0,255)


def tree(len):
    global ang


    x=desings()
    y=desings()
    z=desings()
    t.pencolor(x,y,z)


    if len>=5:
        t.forward(len)
        t.right(ang)
        
        
        tree(len-15)
        
        
        t.lt( 2 * ang)
  

        tree(len-15)
          

          
        t.rt(ang)
        t.fd(-len)



tree(130)

s=turtle.Turtle()
t.penup()
s.hideturtle()
while True:
    s.forward(100)
