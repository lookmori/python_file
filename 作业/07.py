from turtle import *

for j in range(6):
    
    if j%2 == 0:
        fillcolor('red')
    else:
        fillcolor('yellow')
    begin_fill()
    for i in range(3):
        forward(50)
        left(120)
    end_fill()
    left(60)
mainloop()