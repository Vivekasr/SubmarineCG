import turtle

wave = turtle.Turtle()
wave.speed(0)

def waveOutline():
    wave.penup()
    wave.setpos(1000,100)
    wave.pendown()
    wave.pencolor("#506265")
    wave.fillcolor("#9BB5BA")
    wave.begin_fill()
    wave.left(90)
    for i in range(50):
        wave.circle(20,-180)
        wave.left(180)

    wave.end_fill()

    wave.hideturtle()
