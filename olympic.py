import turtle
turtle.pensize(5)
turtle.hideturtle()
thenumber=turtle.numinput('','Enter a number: ')
thenumber=int(thenumber)
turtle.color("blue", "black")
turtle.left(90)
turtle.circle(thenumber)
turtle.right(90)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.color("black", "black")
turtle.right(90)
turtle.circle(thenumber)
turtle.left(90)
turtle.penup()
turtle.forward(2*thenumber+10)
turtle.pendown()
turtle.color("red", "black")
turtle.right(90)
turtle.circle(thenumber)
turtle.penup()
turtle.forward(thenumber/4)
turtle.pendown()
turtle.right(90)
turtle.color("green", "black")
turtle.circle(thenumber)
turtle.penup()
turtle.forward(2*thenumber+10)
turtle.pendown()
turtle.color("yellow", "black")
turtle.circle(thenumber)
