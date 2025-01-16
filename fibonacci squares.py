import random
import turtle


turtle.bgcolor("black") 
t=turtle.Turtle()
t.speed("fastest")
t.hideturtle()

t1=0
t2=1
colour=["Red","Green","Blue","Pink","Black","Yellow","Purple","Violet","Orange","Indigo"]


def fibo():
      global t1
      global t2
      fib=t1+t2
      t1=t2
      t2=fib
      return fib


def sq(a):
      k=clo(colour)
      t.pensize(2)
      j=t.pencolor("white")
      t.fillcolor(k)
      t.begin_fill()
      for n in range(6):
          t.forward(a)
          t.left(90)
      t.end_fill()    
      t.right(90)


def clo(k):
      x=random.choice(k)
      return x


while True:
  side=fibo()
  sq(side)


while True:
    s.forward(50)
()
