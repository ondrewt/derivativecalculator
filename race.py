import turtle
import random
def main():
    turtle.setworldcoordinates(0,0,500,500)
    red = turtle.Turtle()
    blue = turtle.Turtle()
    green = turtle.Turtle()
    red.color('red')
    blue.color('blue')
    green.color('green')
    red.penup()
    blue.penup()
    green.penup()
    red.goto(0,100)
    blue.goto(0,200)
    green.goto(0,300)
    red.shape('turtle')
    blue.shape('turtle')
    green.shape('turtle')
    while red.xcor() < 500 and blue.xcor() < 500 and green.xcor() < 500:
        red.forward(random.randint(1,15))
        blue.forward(random.randint(1,15))
        green.forward(random.randint(1,15))

if __name__ == '__main__':
    main()
