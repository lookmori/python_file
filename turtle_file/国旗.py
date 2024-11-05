import  turtle



def drawwj(x,y,size=20):
    turtle.goto(x,y)
    turtle.seth(-45)
    turtle.pensize(8)
    turtle.pencolor('yellow')
    turtle.pendown()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    for i in range(1,6):
        turtle.forward(size)
        turtle.left(144)
    turtle.end_fill()
    turtle.up()


def drawCf():
    turtle.up()
    turtle.goto(-300,-300)
    turtle.down()
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.seth(0)
    for i in range(1,3):
        turtle.forward(600)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()


drawCf()
drawwj(-100,20)
drawwj(-80,-20)
drawwj(-80,-60)
drawwj(-100,-100)
drawwj(-160,-40,40)


turtle.done()
