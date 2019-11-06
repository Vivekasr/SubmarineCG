import turtle 

sky = turtle.Turtle()
sky.speed(0)

def skyOutline():
    sky.penup()
    sky.setpos(1000,100)
    sky.pendown()
    sky.pencolor("#9BB5BA")
    sky.left(90)
    sky.fillcolor("#9BB5BA")
    sky.begin_fill()
    for j in range(4):
        sky.forward(4000)
        sky.left(90)

    sky.end_fill()

    sky.hideturtle()
    