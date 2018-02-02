import turtle
def main():
    turtle.showturtle()
    rotations = turtle.numinput('','Enter a number: ')
    number = 0
    while rotations > number:
    print ("Drawsquare")
    number = number + 1

def Drawsquare( ):
    rotationangle = 360 / rotations
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.left(rotationangle)
