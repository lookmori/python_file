## turtle 画图

# 导入库
from turtle import *
##画一个正方形

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

## 画正六边形

## 提示 正多边形内角和 （n-2）*180 
## 正多边形每个内角 (n-2) *180 /n
## 转的度数 180 - (n-2) *180 /n


for i in range(6):
    forward(60)
    left(60)

## 画正六边形 填充为红色，画笔为黄色

pencolor('yellow')
fillcolor('red')
begin_fill()
for i in range(6):
    forward(60)
    left(60)
end_fill()


## 画出正六边形 ，单数边为红色，双数边为黄色
for i in range(6):
    if i%2==0:
        color('yellow')
    else:
        color('red')
    forward(60)
    left(60)
