import turtle
turtle.setworldcoordinates(0,0,400,400)
turtle.setpos(0,0)
turtle.penup()
turtle.speed('fast')

def bsquare():
    turtle.color('black','black')
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.end_fill()

def rsquare():
    turtle.color('black','red')
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.end_fill()

def movement():
    turtle.forward(50)

def bloop():
    count = 5
    while count > 1:
        bsquare()
        movement()
        rsquare()
        movement()
        count -= 1

def rloop():
    count = 5
    while count > 1:
        rsquare()
        movement()
        bsquare()
        movement()
        count -= 1

def main():
    bloop()
    turtle.setpos(0,50)
    rloop()
    turtle.setpos(0,100)
    bloop()
    turtle.setpos(0,150)
    rloop()
    turtle.setpos(0,200)
    bloop()
    turtle.setpos(0,250)
    rloop()
    turtle.setpos(0,300)
    bloop()
    turtle.setpos(0,350)
    rloop()




if __name__ == '__main__':
    main()
