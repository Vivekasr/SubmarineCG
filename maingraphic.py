import turtle

from submarine import submarineOutline, submarineInline
from waves import waveOutline
from sky import skyOutline

turtle.bgcolor('#506265')
turtle.speed(0)
turtle.hideturtle()

skyOutline()
waveOutline()
submarineOutline()
submarineInline()

turtle.exitonclick()
