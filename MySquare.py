import turtle


def draw_square():
    print("Hello Square")
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.color("yellow")
    distane=200
    degrees=-90
    counter = 0
    while counter < 4 :
        brad.forward(distane)
        brad.right(degrees)
        counter = counter +1
    window.exitonclick()

draw_square()
