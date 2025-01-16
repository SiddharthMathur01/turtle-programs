import turtle
import random
t = turtle.Turtle()
t.hideturtle()
turtle.Screen().bgcolor("black")
t.pencolor("white")
t.speed("fastest")
turtle.colormode(255)
turtle.colormode(255)
def max():
 return random.randint(0,255)
  
def snowflask():
  t.pensize(2)
  y=320
  for x in range(50):
    for q in range (10):
      
      x=random.randint(-500,500)
      t.penup()
      t.goto(x,y)
      t.pendown()
      s=max()
      d=max()
      f=max()
      t.pencolor(s,d,f)
      for a in range(6):
        t.forward(20)
        t.backward(7.5)#b1
        t.right(40)
        t.forward(10)
        t.backward(10)
        t.left(80)
        t.forward(10)
        t.backward(10)
        t.right(40)
        t.backward(7.5)#b2
        t.right(40)
        t.forward(5)
        t.backward(5)
        t.left(80)
        t.forward(5)
        t.backward(5)
        t.right(40)
        t.backward(5)
        t.right(60) 
    y=y-50
snowflask()