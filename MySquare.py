import turtle

class Hello() :
    
    def __init__(self):
        print("Hello Class in Turtle")

def draw_square():
    print("Hello Square")
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.color("lightblue")
    brad.pensize(2)
    brad.speed(10)
    distance = 200
    degrees = -90
    counter = 0
    rotation = 0
    while rotation < 360:
        brad.right(-1 * rotation)
        print(-1 * rotation)

        while counter < 4:
            brad.forward(distance)
            brad.right(degrees)
            counter = counter + 1

        rotation = rotation + 1
        counter = 0

    window.exitonclick()


Hello();

# draw_square()
