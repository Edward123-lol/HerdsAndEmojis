import turtle

ed = turtle.Turtle()
edd = turtle.Turtle()
eddd = turtle.Turtle()
edddd = turtle.Turtle()

ed.pensize(1)
edd.pensize(1)
eddd.pensize(1)
edddd.pensize(1)

ed.shape("turtle")
edd.shape("turtle")
eddd.shape("turtle")
edddd.shape("turtle")

ed.begin_fill()
ed.color("yellow")
ed.circle(200)
ed.end_fill()

edd.penup()
edd.goto(100, 180)
edd.begin_fill()
edd.color("black")
edd.circle(30)
edd.end_fill()
edd.pendown()

eddd.penup()
eddd.goto(-100, 180)
eddd.begin_fill()
eddd.color("black")
eddd.circle(30)
eddd.end_fill()
eddd.pendown()

edddd.penup()
edddd.goto(0, 75)
edddd.begin_fill()
edddd.color("red")
edddd.circle(50)
edddd.end_fill()


turtle.exitonclick()