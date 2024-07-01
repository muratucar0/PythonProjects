import turtle


screen = turtle.Screen()
screen.title("Turtle Örneği")
screen.bgcolor("white")


t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(1)

def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)


def draw_polygon(sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(50)
        t.right(angle)


t.penup()
t.goto(-50, 0)
t.pendown()

draw_square()

t.penup()
t.goto(100, 0)
t.pendown()

draw_polygon(5)

 
turtle.done()