from turtle import *


## 园在画布中心（0，0）半径是100  红色和蓝色线段都是200 粗细为2


up()
goto(0,-100)
pendown()
circle(100)

up()
goto(100,0)
down()
color('red')
width(2)
goto(-100,0)



up()
goto(0,100)
down()
color('blue')
width(2)
goto(0,-100)


mainloop()