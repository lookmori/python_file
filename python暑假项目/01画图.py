from turtle import *
from random import *
from math import *
class Tree:
    def __init__(self):
        setup(1000, 700)
        bgcolor(1, 1, 1)  # 背景色
        # ht()  # 隐藏turtle
        speed(10)  # 速度 1-10渐进，0 最快
        # tracer(1, 100)    # 设置绘图屏幕刷新频率，参数1设置在正常刷新频次的第参数1次刷新，参数2设置每次刷新的时延
        tracer(0, 0)
        pu()  # 抬笔
        backward(100)
        # 保证笔触箭头方向始终不向下，此处使其左转90度，而不是右转
        left(90)  # 左转90度
        backward(300)  # 后退300
    def tree(self, n, l):
        pd()  # 下笔
        # 阴影效果
        t = cos(radians(heading() + 45)) / 8 + 0.25
        pencolor(t, t, t)
        pensize(n / 1.2)
        forward(l)  # 画树枝
        if n > 0:
            b = random() * 15 + 10  # 右分支偏转角度
            c = random() * 15 + 10  # 左分支偏转角度
            d = l * (random() * 0.25 + 0.7)  # 下一个分支的长度
            # 右转一定角度,画右分支
            right(b)
            self.tree(n - 1, d)
            # 左转一定角度，画左分支
            left(b + c)
            self.tree(n - 1, d)
            # 转回来
            right(c)
        else:
            # 画叶子
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n, n * 0.8, n * 0.8)
            fillcolor(n, n * 0.8, n * 0.8)
            begin_fill()
            circle(3)
            left(90)
            end_fill()
            # 添加0.3倍的飘落叶子
            if random() > 0.7:
                pu()
                # 飘落
                t = heading()
                an = -40 + random() * 40
                setheading(an)
                dis = int(800 * random() * 0.5 + 400 * random() * 0.3 + 200 * random() * 0.2)
                forward(dis)
                setheading(t)
                # 画叶子
                pd()
                right(90)
                n = cos(radians(heading() - 45)) / 4 + 0.5
                pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
                fillcolor(n, n * 0.8, n * 0.8)
                begin_fill()
                circle(2)
                left(90)
                end_fill()
                pu()
                # 返回
                t = heading()
                setheading(an)
                backward(dis)
                setheading(t)
                # pass
        pu()
        backward(l)  # 退回

def select():
    print("***********请选择你要画的选项********")
    print("***********1 佩奇*******************")
    print("***********2 哆啦A梦****************")
    print("***********3 小黄人*****************")
    print("***********4 樱花树*****************")
    input_select = int(input('请输入你的选择：'))
    return input_select

def pig_peiqi():
    import turtle as t
    pensize(4)
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(20)
    # 鼻子
    pu()
    goto(-100, 100)
    pd()
    seth(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)  # 向左转3度
            fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()
    pu()
    seth(90)
    fd(25)
    seth(0)
    fd(10)
    pd()
    pencolor(255, 155, 192)
    seth(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    pu()
    seth(0)
    fd(20)
    pd()
    pencolor(255, 155, 192)
    seth(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    # 头
    color((255, 155, 192), "pink")
    pu()
    seth(90)
    fd(41)
    seth(0)
    fd(0)
    pd()
    begin_fill()
    seth(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    seth(161)
    circle(-300, 15)
    pu()
    goto(-100, 100)
    pd()
    seth(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)  # 向左转3度
            fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()
    # 耳朵
    color((255, 155, 192), "pink")
    pu()
    seth(90)
    fd(-7)
    seth(0)
    fd(70)
    pd()
    begin_fill()
    seth(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    pu()
    seth(90)
    fd(-12)
    seth(0)
    fd(30)
    pd()
    begin_fill()
    seth(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()
    # 眼睛
    color((255, 155, 192), "white")
    pu()
    seth(90)
    fd(-20)
    seth(0)
    fd(-95)
    pd()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    pu()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)
    pd()
    begin_fill()
    circle(3)
    end_fill()
    color((255, 155, 192), "white")
    pu()
    seth(90)
    fd(-25)
    seth(0)
    fd(40)
    pd()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    pu()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)
    pd()
    begin_fill()
    circle(3)
    end_fill()
    # 腮
    color((255, 155, 192))
    pu()
    seth(90)
    fd(-95)
    seth(0)
    fd(65)
    pd()
    begin_fill()
    circle(30)
    end_fill()
    # 嘴
    color(239, 69, 19)
    pu()
    seth(90)
    fd(15)
    seth(0)
    fd(-100)
    pd()
    seth(-80)
    circle(30, 40)
    circle(40, 80)
    # 身体
    color("red", (255, 99, 71))
    pu()
    seth(90)
    fd(-20)
    seth(0)
    fd(-78)
    pd()
    begin_fill()
    seth(-130)
    circle(100, 10)
    circle(300, 30)
    seth(0)
    fd(230)
    seth(90)
    circle(300, 30)
    circle(100, 3)
    color((255, 155, 192), (255, 100, 100))
    seth(-135)
    circle(-80, 63)
    circle(-150, 24)
    end_fill()
    # 手
    color((255, 155, 192))
    pu()
    seth(90)
    fd(-40)
    seth(0)
    fd(-27)
    pd()
    seth(-160)
    circle(300, 15)
    pu()
    seth(90)
    fd(15)
    seth(0)
    fd(0)
    pd()
    seth(-10)
    circle(-20, 90)
    pu()
    seth(90)
    fd(30)
    seth(0)
    fd(237)
    pd()
    seth(-20)
    circle(-300, 15)
    pu()
    seth(90)
    fd(20)
    seth(0)
    fd(0)
    pd()
    seth(-170)
    circle(20, 90)
    # 脚
    pensize(10)
    color((240, 128, 128))
    pu()
    seth(90)
    fd(-75)
    seth(0)
    fd(-180)
    pd()
    seth(-90)
    fd(40)
    seth(-180)
    color("black")
    pensize(15)
    fd(20)
    pensize(10)
    color((240, 128, 128))
    pu()
    seth(90)
    fd(40)
    seth(0)
    fd(90)
    pd()
    seth(-90)
    fd(40)
    seth(-180)
    color("black")
    pensize(15)
    fd(20)
    # 尾巴
    pensize(4)
    color((255, 155, 192))
    pu()
    seth(90)
    fd(70)
    seth(0)
    fd(95)
    pd()
    seth(0)
    circle(70, 20)
    circle(10, 330)
    circle(70, 30)
    exitonclick()


def d_l():
    pensize(8)
    hideturtle()
    screensize(500, 500, bg='white')
    # 猫脸
    fillcolor('#00A1E8')
    begin_fill()
    circle(120)
    end_fill()
    pensize(3)
    fillcolor('white')
    begin_fill()
    circle(100)
    end_fill()
    pu()
    home()
    goto(0, 134)
    pd()
    pensize(4)
    fillcolor("#EA0014")
    begin_fill()
    circle(18)
    end_fill()
    pu()
    goto(7, 155)
    pensize(2)
    color('white', 'white')
    pd()
    begin_fill()
    circle(4)
    end_fill()
    pu()
    goto(-30, 160)
    pensize(4)
    pd()
    color('black', 'white')
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)  # 向左转3度
            fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()
    pu()
    goto(30, 160)
    pensize(4)
    pd()
    color('black', 'white')
    begin_fill()
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)  # 向左转3度
            fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()
    pu()
    goto(-38, 190)
    pensize(8)
    pd()
    right(-30)
    forward(15)
    right(70)
    forward(15)
    pu()
    goto(15, 185)
    pensize(4)
    pd()
    color('black', 'black')
    begin_fill()
    circle(13)
    end_fill()
    pu()
    goto(13, 190)
    pensize(2)
    pd()
    color('white', 'white')
    begin_fill()
    circle(5)
    end_fill()
    pu()
    home()
    goto(0, 134)
    pensize(4)
    pencolor('black')
    pd()
    right(90)
    forward(40)
    pu()
    home()
    goto(0, 124)
    pensize(3)
    pencolor('black')
    pd()
    left(10)
    forward(80)
    pu()
    home()
    goto(0, 114)
    pensize(3)
    pencolor('black')
    pd()
    left(6)
    forward(80)
    pu()
    home()
    goto(0, 104)
    pensize(3)
    pencolor('black')
    pd()
    left(0)
    forward(80)
    # 左边的胡子
    pu()
    home()
    goto(0, 124)
    pensize(3)
    pencolor('black')
    pd()
    left(170)
    forward(80)
    pu()
    home()
    goto(0, 114)
    pensize(3)
    pencolor('black')
    pd()
    left(174)
    forward(80)
    pu()
    home()
    goto(0, 104)
    pensize(3)
    pencolor('black')
    pd()
    left(180)
    forward(80)
    pu()
    goto(-70, 70)
    pd()
    color('black', 'red')
    pensize(6)
    seth(-60)
    begin_fill()
    circle(80, 40)
    circle(80, 80)
    end_fill()
    pu()
    home()
    goto(-80, 70)
    pd()
    forward(160)
    pu()
    home()
    goto(-50, 50)
    pd()
    pensize(1)
    fillcolor("#eb6e1a")
    seth(40)
    begin_fill()
    circle(-40, 40)
    circle(-40, 40)
    seth(40)
    circle(-40, 40)
    circle(-40, 40)
    seth(220)
    circle(-80, 40)
    circle(-80, 40)
    end_fill()
    # 领带
    pu()
    goto(-70, 12)
    pensize(14)
    pencolor('red')
    pd()
    seth(-20)
    circle(200, 30)
    circle(200, 10)
    # 铃铛
    pu()
    goto(0, -46)
    pd()
    pensize(3)
    color("black", '#f8d102')
    begin_fill()
    circle(25)
    end_fill()
    pu()
    goto(-5, -40)
    pd()
    pensize(2)
    color("black", '#79675d')
    begin_fill()
    circle(5)
    end_fill()
    pensize(3)
    right(115)
    forward(7)
    mainloop()


def yellow_people():
    colormode(255)
    hideturtle()
    speed(0)
    penup()
    pensize(4)
    goto(100,0)
    pendown()
    left(90)
    color((0,0,0),(255,255,0))
    #身体绘制上色
    begin_fill()
    forward(200)
    circle(100,180)
    forward(200)
    circle(100,180)
    end_fill()
    #右眼睛绘制上色
    pensize(12)
    penup()
    goto(-100,200)
    pendown()
    right(100)
    circle(500,23)
    pensize(3)
    penup()
    goto(0,200)
    pendown()
    seth(270)
    color("black","white")
    begin_fill()
    circle(30)
    end_fill()
    penup()
    goto(15,200)
    pendown()
    color("black","black")
    begin_fill()
    circle(15)
    end_fill()
    penup()
    goto(35,205)
    color("black","white")
    begin_fill()
    circle(5)
    end_fill()
    #左眼睛绘制上色
    pensize(3)
    penup()
    goto(0,200)
    pendown()
    seth(90)
    color("black","white")
    begin_fill()
    circle(30)
    end_fill()
    penup()
    goto(-15,200)
    pendown()
    color("black","black")
    begin_fill()
    circle(15)
    end_fill()
    penup()
    goto(-35,205)
    color("black","white")
    begin_fill()
    circle(5)
    end_fill()
    #嘴绘制上色
    penup()
    goto(-20,100)
    pendown()
    seth(270)
    color("black","white")
    begin_fill()
    circle(20,180)
    left(90)
    forward(40)
    end_fill()
    #裤子绘制上色
    penup()
    goto(-100,0)
    pendown()
    seth(0)
    color("black","blue")
    begin_fill()
    forward(20)
    left(90)
    forward(40)
    right(90)
    forward(160)
    right(90)
    forward(40)
    left(90)
    forward(20)
    seth(270)
    penup()
    goto(-100,0)
    circle(100,180)
    end_fill()
    #左裤子腰带
    penup()
    goto(-70,20)
    pendown()
    color("black","blue")
    begin_fill()
    seth(45)
    forward(15)
    left(90)
    forward(60)
    seth(270)
    forward(15)
    left(40)
    forward(50)
    end_fill()
    left(180)
    goto(-70,30)
    dot()
    #右裤腰带
    penup()
    goto(70,20)
    pendown()
    color("black","blue")
    begin_fill()
    seth(135)
    forward(15)
    right(90)
    forward(60)
    seth(270)
    forward(15)
    right(40)
    forward(50)
    end_fill()
    left(180)
    goto(70,30)
    dot()
    #脚
    penup()
    goto(4,-100)
    pendown()
    seth(270)
    color("black","black")
    begin_fill()
    forward(30)
    left(90)
    forward(40)
    seth(20)
    circle(10,180)
    circle(400,2)
    seth(90)
    forward(20)
    goto(4,-100)
    end_fill()
    penup()
    goto(-4,-100)
    pendown()
    seth(270)
    color("black","black")
    begin_fill()
    forward(30)
    right(90)
    forward(40)
    seth(20)
    circle(10,-225)
    circle(400,-3)
    seth(90)
    forward(21)
    goto(-4,-100)
    end_fill()
    #左手
    penup()
    goto(-100,50)
    pendown()
    seth(225)
    color("black","yellow")
    begin_fill()
    forward(40)
    left(90)
    forward(35)
    seth(90)
    forward(50)
    end_fill()
    #右手
    penup()
    goto(100,50)
    pendown()
    seth(315)
    color("black","yellow")
    begin_fill()
    forward(40)
    right(90)
    forward(36)
    seth(90)
    forward(50)
    end_fill()
    #
    penup()
    goto(0,-100)
    pendown()
    forward(30)
    #
    penup()
    goto(0,-20)
    pendown()
    color("yellow")
    begin_fill()
    seth(45)
    forward(20)
    circle(10,180)
    right(90)
    circle(10,180)
    forward(20)
    end_fill()
    #
    penup()
    color("black")
    goto(-100,-20)
    pendown()
    circle(30,90)
    penup()
    goto(100,-20)
    pendown()
    circle(30,-90)
    #头顶
    penup()
    goto(2,300)
    pendown()
    begin_fill()
    seth(135)
    circle(100,40)
    end_fill()
    penup()
    goto(2,300)
    pendown()
    begin_fill()
    seth(45)
    circle(100,40)
    exitonclick()






flag = True
while flag:
    options = select()
    match options:
        case 1:
            pig_peiqi()
        case 2:
            d_l()
        case 3:
            yellow_people()
        case 4:
            tree = Tree()
            tree.tree(12, 100)  # 递归7层
            done()
    