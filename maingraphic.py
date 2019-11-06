import turtle

from submarine import submarineOutline
from waves import waveOutline
from sky import skyOutline

turtle.bgcolor('#506265')
turtle.speed(0)

skyOutline()
waveOutline()
submarineOutline()

turtle.hideturtle()
turtle.exitonclick()
