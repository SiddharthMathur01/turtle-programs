import turtle
turtle.bgcolor("light grey")
r=turtle.Turtle()
r.speed("fast")
r.shape("turtle")
r.pensize(4)
r.penup()
r.goto(-50,0)
r.pendown()
for i in range(4):#face of the robot
  r.forward(100)
  r.left(90)
r.penup()
r.goto(-10,0)
r.right(90)
r.pendown()
for j in range(2):#neck of the robot
  r.forward(30)
  r.left(90)
  r.forward(20)
  r.left(90)
''' Task 2: '''
print()
print("***** Task 2: *****")
r.penup()
r.goto(-100,-30)
r.setheading(0)
r.pendown()
for a in range(3):#robot body
  r.forward(200)
  r.right(90)
  r.forward(150)
  r.right(90)


r.penup()
r.goto(-100,-30)
r.setheading(180)
r.pendown()
for q in range(3):#robo left shoulder
  r.forward(10)
  r.left(90)
  r.forward(25)
  r.left(90)
r.left(90)
r.forward(25)
r.left(90)
for w in range(3):#robo left arm
  r.forward(30)
  r.left(90)
  r.forward(170)
  r.left(90)
r.backward(5)
for e in range(4):#robo left hand
  r.forward(40)
  r.right(90)
  r.forward(55)
  r.right(90)
r.penup()
r.goto(-130.5,-215)
r.pendown()
for t in range(3):#robo left thumb
  r.forward(10)
  r.right(90)
  r.forward(30)
  r.right(90)

r.penup()
r.goto(100,-30)
r.setheading(0)
r.pendown()
for q in range(3):#robo left shoulder
  r.forward(10)
  r.right(90)
  r.forward(25)
  r.right(90)
r.right(90)
r.forward(25)
r.right(90)
for w in range(3):#robo left arm
  r.forward(30)
  r.right(90)
  r.forward(170)
  r.right(90)
r.backward(5)
for e in range(4):#robo left hand
  r.forward(40)
  r.left(90)
  r.forward(55)
  r.left(90)
r.penup()
r.goto(130.5,-215)
r.pendown()
for t in range(3):#robo left thumb
  r.forward(10)
  r.left(90)
  r.forward(30)
  r.left(90)


r.penup()
r.goto(-80,-180)
r.pendown()
for u in range(3):#robo lower body
  r.forward(160)
  r.right(90)
  r.forward(50)
  r.right(90)
r.penup()
r.goto(-60,-230)
r.pendown()
for o in range(3):#robo left leg
  r.left(90)
  r.forward(170)
  r.left(90)
  r.forward(40)
r.setheading(180)
r.backward(5)
for s in range(3):#robo left toe
  r.forward(50)
  r.left(90)
  r.forward(40)
  r.left(90)
r.penup()
r.goto(60,-230)
r.pendown()
for p in range(3):#robo right leg
  r.right(90)
  r.forward(170)
  r.right(90)
  r.forward(40)
r.setheading(0)
r.backward(5)
for d in range(3):#robo right toe
  r.forward(50)
  r.right(90)
  r.forward(40)
  r.right(90)


r.penup()
r.goto(-30,70)
r.pendown()
r.circle(10)#robo left eye
r.penup()
r.backward(60)
r.pendown()
r.circle(10)#robo right eye
r.penup()
r.goto(200,200)
r.pendown()