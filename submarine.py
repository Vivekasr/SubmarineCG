import turtle 

subOut = turtle.Turtle()
subOut.speed(0)

def submarineOutline():

    subOut.penup()
    subOut.setpos(150,-100)
    subOut.fillcolor("#fafafa")
    subOut.begin_fill()
    subOut.pendown()
    subOut.pencolor("black")
    subOut.circle(80,180) #subCockpit
    subOut.forward(30)    #sublength = 50+30
    subOut.right(180)
    subOut.circle(20,-90)   #sublength = 50+30+20
    subOut.right(180)
    subOut.forward(50)
    subOut.right(180)
    subOut.circle(10,-90)
    subOut.right(180)
    subOut.forward(15)
    subOut.left(90)
    subOut.forward(20)
    subOut.left(90)
    subOut.forward(30)     #sublength = 50 + 30 + 20 + 20 + 10 + 15
    subOut.circle(15,90)
    subOut.forward(65)
    subOut.right(90)
    subOut.forward(85)      #sublength = 50 + 30 + 20 + 20 +10 + 15 + 85
    subOut.circle(20,90)
    subOut.right(90)
    subOut.forward(70)      #sublength = 50 + 30 + 20 + 20 + 10 + 15 + 85 + 10 + 70
    subOut.circle(50,90)
    subOut.right(90)
    subOut.circle(55,180)
    subOut.forward(150)
    subOut.right(90)
    subOut.circle(40,180)
    subOut.right(90)
    subOut.forward(75)
    subOut.end_fill()

    subOut.hideturtle()

    


    

